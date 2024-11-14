from google.api_core.client_options import ClientOptions
from google.cloud import documentai

#projects/52285717409/locations/us/processors/af04720a222005a2
def create_processor(project_id, location, processor_display_name, processor_type):
    
    #Setting up an API Endpoint
    opts = ClientOptions(api_endpoint = f"{location}-documentai.googleapis.com")
    
    #Creating a client
    client = documentai.DocumentProcessorServiceClient(client_options = opts)
    
    #Defining which project we are working on
    parent = client.common_location_path(project_id, location)
    
    #Creating a processor
    processor = client.create_processor(
        parent = parent,
        processor = documentai.Processor(
            display_name = processor_display_name,
            type_ = processor_type
        )
    )
    
    print(f"Processor Name: {processor.name}")
    print(f"Processor Display Name: {processor.display_name}")
    print(f"Processor Type: {processor.type_}")
    print(f"Processor ID: {processor.id}")
    

def main():
    
    PROJECT_ID = "alert-arbor-441718-d8"
    LOCATION = 'us'
    PROCESSOR_DISPLAY_NAME = "LectureSummarizer"
    PROCESSOR_TYPE = "SUMMARY_PROCESSOR"
    
    create_processor(project_id=PROJECT_ID, 
                    location=LOCATION,
                    processor_display_name=PROCESSOR_DISPLAY_NAME,
                    processor_type=PROCESSOR_TYPE)
    
if __name__ == "__main__":
    main()