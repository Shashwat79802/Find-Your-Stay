# Find Your Stay

<img src="https://github.com/poorvadiwan/Find-Your-Stay-1/blob/master/MiniProject/logo.png" align="right"
alt="logo" width = "35%">

<div align="justify">
FindYourStay is a web application that helps users search for hotel stays at their desired travel location in one go. 
It cuts the chase of looking for hotels on different websites by bringing it all in one platform. We like to call it - 
<b>“The Stay Search Engine”</b>. 
</div>

### How does it work?

  1. The site takes the location query from the user in the format - ‘City, State’.</li>
  2. Relevant data from sites like [oyorooms.com](https://www.oyorooms.com) and [yatra.com](https://www.yatra.com) is scrapped in real-time and stored in a csv files.
      Data fields include - Hotel Name, Price, Images, Address, Ratings, and Hotel URL.
  3. This data is reflected on the site ready for the user to interact.
  4. Filter features like sorting on the basis of popularity and relevance are included for better results. 


Here are a few snippets of the website - 
<br><br>
<img src="https://github.com/poorvadiwan/Find-Your-Stay-1/blob/master/MiniProject/home%20page.png" 
alt="homepage" width = "80%" align="center">
<br><br>
<img src="https://github.com/poorvadiwan/Find-Your-Stay-1/blob/master/MiniProject/about.png" 
alt="homepage" width = "80%" align="center">
<br><br>
<img src="https://github.com/poorvadiwan/Find-Your-Stay-1/blob/master/MiniProject/search.png" 
alt="homepage" width = "80%" align="center">
<br><br>
<b>The project is open source and all suggestions and amendments are welcome from the community. Here is a guide to help you install.</b>

### Pre-requisites -
**Code editor, Python (latest version).**

1. Fork the repository.
  
2. To clone the repository to your local system, navigate to the folder where you want to save the project and run the command-
    <br>
    `git clone https://github.com/your-github/Find-Your-Stay.git`
  
3. Now navigate to the root folder of the project where the “manage.py” file is located.
  
4. Create a virtual environment using the command-
    <br>
    `python3 -m virtualenv env_name`
    <br>
    **Note:** You can name the virtual environment at your convenience.
  
5. To activate the virtual environment, use the command- <br>
  `env_name/scripts/activate`
  
6. And now to install all the project-related dependencies, run the command in the root folder- <br>
  `pip3 install -r Requirements.txt`
  
7. To run the application, use the command- <br>
  `python3 manage.py runserver`
  
This runs the project on your local host. To stop use the server ‘CTRL + C’.
<br>
### Thanks for visiting!! 
