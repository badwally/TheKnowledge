---
schema_version: 1
id: yt-3JqJkRF0_yU
type: youtube
title: How to Set up HubSpot to BigQuery integration | Tutorial
url: https://www.youtube.com/watch?v=3JqJkRF0_yU
authors:
- Coupler․io Academy
ingested_at: '2026-05-28T14:04:50Z'
content_hash: sha256:94ea575e19c33eea9f25be265c8dda1c6f07eb8c7248e6b0d7b694a240940fb1
domains:
- orita-cmo
nlm_corpus_ids:
- adc34eb9-c798-4530-8b0d-4b166a0bc38a
wiki_pages:
- wiki/entities/coupler-io.md
- wiki/entities/bigquery.md
meta:
  channel: Coupler․io Academy
  channel_url: https://www.youtube.com/@coupleracademy
  duration_seconds: 237
  caption_track: fetched
  snippet_count: 50
filter:
  score: 0.7
---
[8] Hi! I'm Alina from Coupler.io
[10] Today I'll show you how to set up HubSpot to BigQuery integration.
[14] For a start, log in to use the software.
[20] In the top-left corner, click the "Add new 
importer" button.
[23] Name the importer. I'll go by the name "HubSpot deals".
[27] Now I need to fill out the data source parameters.
[30] From the drop-down menu, select HubSpot. Click "Continue".
[34] To be able to pull data from this app, you need to connect your HubSpot account, so click "Connect".
[40] Log in to the account that you want to import data from.
[45] Choose the account and close the pop-up window. Сlick "Continue".
[50] Select the data category to export from the drop-down menu.
[52] I'll pick "Deals" since I want to import this information to BigQuery.
[57] By default all the fields from HubSpot 
will be imported: both basic and custom.
[62] But you can filter what custom fields to import by adding the internal names of those fields from
[66] HubSpot into this setting.
[68] Make sure to enter each of them in a new line.
[71] If you want to filter your data by creation date, you can specify the "Start date" using this setting.
[77] Now it's time to set up your destination.
[78] From the drop-down menu, select 
BigQuery as the system you want to import data to.
[83] As you can see, you can also use Coupler.io 
to import your HubSpot data to Google Sheets and Microsoft Excel.
[89] Now connect your BigQuery destination account.
[93] To be able to import data to BigQuery, you need to select a key file in JSON format.
[97] Here's how to get it. Go to the Google Cloud platform console.
[102] In the navigation menu on the left-hand side, select "IAM & Admin", then select "Service accounts".
[107] Click "Create service account" at the top. 
Enter the service account name and click "Create".
[114] Add roles: "BigQuery data editor" and "BigQuery job user".
[119] Click "Continue" and then "Done".
[124] Click on the three dots of a service 
account and choose "Manage keys".
[128] Press "Add key" and select "Create new 
key", choose JSON type and press "Create".
[136] The file will be saved to your computer.
[139] Now go back to the Coupler.io form and select this file.
[147] Click "Save" and "Continue". So I've just connected to BigQuery account.
[152] Now it's time to specify the dataset and the table where I will import my data to.
[157] To do it I open BigQuery.
[166] I copy the name of the dataset 
and paste it into this field.
[171] Then I do the same with the table name and press "Continue".
[177] This is the default setting that I'm not 
going to change, so i'll just click "Continue".
[182] Here I will set up a schedule for an automatic data refresh.
[185] Switch the toggle "on".
[187] I want to pull data to BigQuery on an hourly basis, every day of the week.
[190] So I'm making a small amendment to the suggested schedule selecting Saturday and 
Sunday.
[195] Both the time preferences and the time zone are correct, so I won't change them.
[200] The final step is to click "Save and run".
[213] To see the imported dataset, click 
"View results" in the top-right corner.
[221] That's how you do it!
[222] Set up your HubSpot to BigQuery integration in just 5 minutes with no coding skills required.
[227] Coupler.io has got you covered!
[229] Thanks for watching!
[230] Check out other tutorials in this playlist!
[234] If you have any questions, feel free to contact our support!
