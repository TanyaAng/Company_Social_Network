## COMPANY SOCIAL NETWORK

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">API endpoints</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


### About The Project
  DJANGO REST application for a Company Social Network:
 - login, register and logout functionally - token authentication and "sandboxed" user after registration;
 - extended Django User model;
 - allows CRUD operations to profile entities;
 - allows CRUD operations to posts entities - prodived "soft delete" for posts and automatically delete old posts in every 10 days;
 - like post functionality - user can like or dislike every posts;
 
  
<p align="right"><a href="#top">back to top</a></p>

#### Build With
* [Python](https://www.python.org/)
* [Django REST Framework](https://www.django-rest-framework.org/)


### Getting Started
#### Installation
1. Clone the repo
   ```sh
   https://github.com/TanyaAng/Company_Social_Network.git
   ```
2. Install all Python libraries
   ```sh
   pip install -r requirements.txt
   ```

<p align="right"><a href="#top">back to top</a></p>

### Usage
1. Run cron
     ```sh
   python manage.py runcron
   ```


<p align="right"><a href="#top">back to top</a></p>

### API endpoints

| Datapoint              | HTTP Method | Description                       |
|------------------------|-------------|-----------------------------------|
| /login/                | POST        | login                             |
| /register/             | POST        | register new account              |
| /logout/               | GET         | logout                            |
| /logout/               | POST        | logout                            |
| /profile/              | POST        | create profile of current user    |
| /profile/{profile_id}/ | GET         | get profile of current user       |
| /profile/{profile_id}/ | PUT         | update profile of current user    |
| /posts/                | GET         | get list of all posts             |
| /posts/                | POST        | create new post from current user |
| /posts/{post_id}/      | GET         | get a post information            |
| /posts/{post_id}/      | DELETE      | delete a post                     |




<p align="right"><a href="#top">back to top</a></p>

### License
MIT License

<p align="right"><a href="#top">back to top</a></p>

### Contact

Tanya Angelova - [LinkedIn](https://www.linkedin.com/in/tanya-angelova-44b03590/) - t.j.angelova@gmail.com

Project Link: [github link]

<p align="right"><a href="#top">back to top</a></p>

[LinkedIn]: https://www.linkedin.com/in/tanya-angelova-44b03590/
[github link]: https://github.com/TanyaAng/Company_Social_Network