from fastapi import APIRouter,UploadFile,File,Depends
from app.dependencies import get_document_service
from app.services.document_service import DocumentService

router = APIRouter(prefix="/documents",tags=["Documents"])

@router.post("/upload")
async def upload_document(file:UploadFile = File(...),document_service:DocumentService=Depends(get_document_service)):
    result = await document_service.upload(file)
    return result

@router.get("")
def get_documents(document_service:DocumentService=Depends(get_document_service)):
    return document_service.get_documents()

@router.get("/{document_id}")
def get_document(document_id: int,document_service: DocumentService = Depends(get_document_service)):
    return document_service.get_document(document_id=document_id)