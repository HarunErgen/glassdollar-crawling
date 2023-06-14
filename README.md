# GlassDollar Crawling

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/glassdollar-crawling.git

2. Build the docker image:

docker build -t glassdollar-crawling .

3. Run the Docker container:

docker run -d -p 80:80 glassdollar-crawling

4. Access the web application at http://localhost:80 in your browser.

## Usage

Root endpoint (/): Displays a "Fetching in progress..." message while the data is being fetched.  
Corporate results endpoint (/corporate_results): Displays the fetched data when the fetching process is completed.