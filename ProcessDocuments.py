from google.api_core.client_options import ClientOptions
from google.cloud import documentai

def ProcessDocuments(project_id, location, path_to_file, processor_name):
    
    #Processor already created one in CreateProcessor.py
    
    # Processor Name: projects/52285717409/locations/us/processors/af04720a222005a2
    # Format: projects/{project_id}/locations/{api_endpoint_location}/processors/{processor_id}
    
    opts = ClientOptions(api_endpoint = f"{location}-documentai.googleapis.com")
    client = documentai.DocumentProcessorServiceClient(client_options = opts)
    
    #Opening PDF file
    with open(path_to_file, 'rb') as file:
        file_content = file.read()
        
    print("Succesfully Opened and Read the File")
    
    raw_document = documentai.RawDocument(
        content = file_content,
        mime_type = "application/pdf"
    )
    request = documentai.ProcessRequest(name = processor_name,
                                        raw_document = raw_document)
    
    result = client.process_document(request = request)
    
    document = result.document
    
    print(document.text)

def main():
    ProcessDocuments("52285717409",
                    "us",
                    '/Users/harshgarg/Downloads/Human Rights Lecture-3_removed.pdf',
                    "projects/52285717409/locations/us/processors/af04720a222005a2")

if __name__ == "__main__":
    main()