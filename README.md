# Python Behave XML Framework
python , behave , Selenium webdriver (Optional)
Tested on Python 2.7.10 & 3.4.2 and all libraries installed with the pip that came with 3.4.2  

# Pre-requistie
1. Clone the Repository
2. Install Python 2.7 or higher.
3. Install pip
4. Installing all the dependencies - pip install -r requirements.txt

# Usage  
1. Open a shell/command prompt and from the root folder 
   run "behave features --no-capture -D XPATHKEY=myaccountpage.buy_pass_button,myaccountpage.focused_button -D SOURCEXML=./features/data/MyAccount.xml"  
2. Run behave with "-v" gives verbose log.
3. Example Usage:
    * behave features --no-capture -D XPATHKEY=myaccountpage.focused_button -D SOURCEXML=./features/data/MyAccount.xml
    * behave features --no-capture -D XPATHKEY=myaccountpage.buy_pass_button -D SOURCEXML=./features/data/MyAccount.xml
   
