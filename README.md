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
4. Access the web application at http://localhost:80 in your browser.

## Usage
Root endpoint (/): Displays a "Fetching in progress..." message while the data is being fetched.
Corporate results endpoint (/corporate_results): Displays the fetched data when the fetching process is completed.
