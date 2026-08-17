from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
 
def load_and_chunk_pdf(file_path, chunk_size = 1000, chunk_overlap = 100):
    """
    This function Load a PDF File using pypdfloader and chunk them in
    manageable sizes.

    Args:
        file_path (str): Path to the PDF file.
        chunk_size (int): Size of each chunk.
        chunk_overlap (int): Overlap between chunks.
    
    Returns:
        list: List of chunks.
    """
    #initialize loader
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap
    )
    
    chunks = text_splitter.split_documents(documents)

    return chunks