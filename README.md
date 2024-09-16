# Cron Job for Bitcoin News Scraping
## Description
This file provides information on how to set up and run a scheduled task using the scheduler library to automate the execution of the Bitcoin news scraper ```Utoday_website.py```. The scraper extracts the latest Bitcoin news from U.Today Bitcoin News and stores the following fields:
- News_Title: The title of the news article.
- News_Date: The date the article was published.
- News_Source_url: The URL of the news article.

The cron job ```cron_job.py ```is configured to run every Sunday at midnight to scrape news from the last seven days.
## Files
Utoday_website.py: The main scraping script that extracts the news data.
cron_job.py: This file contains the scheduling logic that automatically triggers Utoday_website.py every Sunday at midnight.
## Requirements
Ensure you have the following Python packages installed:
- schedule: Used for scheduling the scraping job.
- Selenium: Used for web scraping.
To install these dependencies, run:
```
pip install schedule selenium
```
## Usage
1. Manually Running the Scraping Script
If you want to manually run the scraping process, execute the Utoday_website.py file directly:
```
python Utoday_website.py
```
2. Setting up the Cron Job ```cron_job.py```.
The cron_job.py file is designed to automate the execution of the scraper every Sunday at midnight. It uses the schedule library to handle the timing of the job.

- Running the Scheduled Task:
- Ensure that the Utoday_website.py path is correctly set in cron_job.py.

Run the cron_job.py script to start the scheduler:
```
python cron_job.py
```
This will keep the script running in the background, and the scraping task will be triggered every Sunday at midnight.

## Logging
The cron_job.py script will also create a log file ```cron_log.txt```that records the execution time and status of the scraping job each time it runs. Check this log file for any issues or confirmation of a successful run.

## Future Enhancements
- Improve logging to include detailed error messages in case of failures.
- Add email notifications or alerts for task completion.
- Let me know if you need further adjustments!