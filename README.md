# Email-Automated-Dashboard

Open up a terminal and clone this repo using the following line:

git clone https://github.com/zevbo/Email-Automated-Dashboard.git

Then, go to https://pi.pardot.com/email/report and click on tools
Select "Export all items to CSV"
This will download an export.csv file, probably to your downloads folder

Open up this file with numbers and delete all of the columns except for the following:
Name, Subject,Sent On,Sent,Unique Opens,Unique Clicks,Opt Outs

Once you hit save, you will need to go to file, export to, CSV. Make sure you save it to Email-Automated-Dashboard and it is called export

If you have done this before, you may want to delete all of the data from the dashboard.csv file as to clear the clutter.

Now, go back to the terminal and go into the Email-Automated-Dashboard folder by typing in:
cd Email-A
And then hitting tab.

Now, write the following(but don't hit enter just yet):
python email
Then hit tab. Now write the year and then the month, and then you can hit enter.
The line should look something like this:

pythom email-to-dashboard 2018 7

Finally, open dashboard.csv with numbers and copy all of the data and paste it into the dashboard
