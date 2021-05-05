# ENSEMBL REST WEB SERVICE  

**API SPECIFICATIONS**  

**Name** : `/gene_suggest`  
**Method** : GET  
**Description** : Get a list of genome display labels from ensembl database  
**Required Parameters** :  
1. **query**  
   Data Type : string  
   Description : any valid string from the display labels  
2. **species**  
   Data Type : string  
   Description : any valid species name  
3. **limit**  
   Data Type : integer  
   Description : the number of suggestions to return  
  
**DEPLOYMENT**
1. For cloud based deployment various PaaS and IaaS providers support Django app deployment eg:- [Heroku](https://devcenter.heroku.com/articles/deploying-python), [PythonAnywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/), [Amazon Web Services](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html) etc.    
2. For now, the application has been hosted on Heroku with free resources, since it is a POC. 
3. Scaling up with the increase in traffic can be solved by using load balancer and caching the most searched responses, in case the data is static otherwise, the one that requires most time to load.
4. To view the working application with parameters set to 'brc', 'gorilla_gorilla' and 10 respectively [click here](https://ensembl.herokuapp.com/gene_suggest?query=brc&species=gorilla_gorilla&limit=10).  
5. For deployment on heroku these steps followed:    
   * A Procfile with  
     `web: gunicorn ensembl.wsgi --log-file -`  
   * A requirements.txt file with all the requirements including **gunicorn** and **whitenoise** specifically required for heroku  
     `pip freeze > requiremets.txt`  
   * Updating settings.py with  
     `STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'`  
   * On heroku dashboard create a new app and use Github as Deployment method
   * Connect the repository for the app  
   * Deploy branch, if Automatic Deploys is enabled, Heroku automatically deploys on every push to the branch selected  

**TESTING**  
1. For testing tests.py is already loaded with 5 test cases. But Django TestCase can't be used as it requires read and write permissions to the database.
2. POSTMAN can be used for api testing.  
