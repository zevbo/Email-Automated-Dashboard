# Email-Automated-Dashboard

Open up a terminal and clone this repo using the following line:

git clone https://github.com/zevbo/Email-Automated-Dashboard.git

Then, go to https://pi.pardot.com/email/report and click on tools
Select "Export all items to CSV"
This will download an export.csv file. If it goes into export(1).csv it means you already have an export.csv file. Delete the old export.csv file and redownload the new one from pardot.

If you have done this before, you may want to delete all of the data from the dashboard.csv file as to clear the clutter.

Now, go back to the terminal and go into the Email-Automated-Dashboard folder by typing in:

cd Email-Automated-Dashboard

Now, write the following(but don't hit enter just yet):

python email

Then hit tab. Now write the year and then the month, and then you can hit enter.
The line should look something like this:

python email-to-dashboard 2018 07
python email-to-dashboard 2017 11

Finally, open dashboard.csv with numbers(or any app for visualizing csv files) and copy all of the data and paste it into the dashboard
