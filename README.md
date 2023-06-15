# GlassDollar Crawling

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HarunErgen/glassdollar-crawling.git
   ```

2. Build the Docker image:
   ```bash
   docker build -t glassdollar-crawling .
   ```
3. Run the Docker container:
   ```bash
   docker run -d -p 80:80 glassdollar-crawling
   ```

## Usage
### On Browser
1) Open the root endpoint at http://localhost:80/ 
2) Click on the "Start Fetch" button. A POST request will be created on the /start_fetch endpoint.  
   ![image](https://github.com/HarunErgen/glassdollar-crawling/assets/83069560/687767a0-9078-462c-a9a6-31585e64b40f)
3) You will be redirected to the /fetch_status endpoint. By refreshing the page (sending a GET request to /fetch_status), you can see the updated values of "corporate_count" and "fetch_status". 
 
<img src="https://github.com/HarunErgen/glassdollar-crawling/assets/83069560/e193f02b-5164-4a08-a5d5-d3d555e5c6a3"/>  
<img src="https://github.com/HarunErgen/glassdollar-crawling/assets/83069560/1988d86f-5e74-4f45-9d40-8c97e24fe70f"/>  
<img src="https://github.com/HarunErgen/glassdollar-crawling/assets/83069560/714a860b-7b16-463a-81bd-2e5a3eb87099"/>  


4) Once the fetch_status is "done", you can send a GET request to /corporate_results and see the JSON result.  
<img src="https://github.com/HarunErgen/glassdollar-crawling/assets/83069560/643de396-d2be-40b4-889a-144435ca19ef" width="450" height="300" />  

5) You can re-fetch by going back to the root.

### On FastAPI docs
1) Go to http://localhost:80/docs.
2) Execute POST /start_fetch.
3) Execute GET /fetch_status to see the current status.
4) Execute GET /corporate_results when the fetching is complete.

## Responses
### 1) POST /start_fetch:  

![image](https://github.com/HarunErgen/glassdollar-crawling/assets/83069560/e055b9a8-443a-4797-984c-a27a386418ee)  

### 2) GET /fetch_status while fetching:  

![image](https://github.com/HarunErgen/glassdollar-crawling/assets/83069560/3c54d4a0-64d4-4f9f-aa09-8ca7de055754)  

### 3) GET /fetch_status after completion:  

![image](https://github.com/HarunErgen/glassdollar-crawling/assets/83069560/5de5f4b0-af0b-4057-aff6-e0f35680cc5b)  

### 4) GET /corporate_results while fetching:  

![image](https://github.com/HarunErgen/glassdollar-crawling/assets/83069560/2322a42b-6959-44bb-96ab-233511aec38e)  

### 5) GET /corporate_results after fetching:  

![image](https://github.com/HarunErgen/glassdollar-crawling/assets/83069560/2d60cd8c-dfd2-4eca-8c32-c89c7c1856a4)




