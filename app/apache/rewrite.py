import os

from dotenv import load_dotenv

load_dotenv()

httpd_path = os.getenv("HTTPD_PATH")

print("OPTION:1 - Block Reffering URLs \nOPTION:2 - Enable .htaccess in apache \nOPTION:3 - Redirects incase of error encountered")
choice1=input("Ypur choice: ")


# Block multiple  URLs from accessing content 


if choice1 == "1":

    directory=input("Rewrite directory: ")
    add_another= "Y"
    f = open(directory+"/.htaccess", "a")
    f.write("\n<IfModule mod_rewrite.c>\n")
    f.write("RewriteEngine on\n")

    while add_another=="y" or add_another=="Y":
       URL=input("Enter the Url:")
       f.write("\nRewriteCond %{HTTP_REFERER} "+URL+" [NC ,OR]")
       add_another=input("Do you want add another url to blocklist:(Y/N) ")
    f.write("\nRewriteCond %{HTTP_REFERER} "+URL+" [NC]")
    f.write("\nRewriteRule .* - [F]")
    f.write("\n</IfModule>\n")
    f.close()




# Enable override in apache2.conf



elif choice1 == "2":
   
    directory=input("Working directory: ")
    f=open(httpd_path, "a")
    overide_condition="\n<Directory "+directory+">\nOptions Indexes FollowSymLinks\nAllowOverride All\nRequire all granted\n</Directory>\n"
    f.write(overide_condition)
    f.close()




# Re-Direct incase of error



else:
    directory=input("Rewrite directory: ")
    f = open(directory+"/.htaccess", "w")

    # redirection for error code:
    # 400,401,403,404,500
    f.write("ErrorDocument 400 /error/bad-request.html \nErrorDocument 401 /error/unauthorised.html \nErrorDocument 403 /error/forbidden.html \nErrorDocument 404 /error/file-not-found.html \nErrorDocument 500 /error/internal-server-error.html")
    
    f.close()
    
    # Redirecting to directory
    try:
       os.mkdir(directory+"/error")
       print("/error directory has been made \n")
    except:
       print("/error directory exists \n")
    
    # Error Code 400
    
    f=open(directory+"/error/bad-request.html", "w")
    f.write(" <--Error Code 400-->")
    f.close()

    # Error Code 401

    f=open(directory+"/error/unauthorised.html", "w")
    f.write(" <--Error Code 401-->")
    f.close()

    # Error Code 403

    f=open(directory+"/error/forbidden.html", "w")
    f.write(" <--Error Code 403-->")
    f.close()

    # Error Code 404

    f=open(directory+"/error/file-not-found.html", "w")
    f.write(" <--Error Code 404-->")
    f.close()

    # Error Code 500

    f=open(directory+"/error/internal-server-error.html", "w")
    f.write(" <--Error Code 500-->")
    f.close()


   


os.system("systemctl restart apache2")