docker build -t schoolwebapp .
docker run -d -p 80:80 --rm --name app-school schoolwebapp
# docker run -d -p 80:80 --rm -v $(pwd):/var/www/apache-flask --name app-school schoolwebapp
