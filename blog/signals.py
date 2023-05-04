from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_init, pre_delete, post_delete, post_init, post_save, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

@receiver(user_logged_in, sender= User)
def login_success(sender, request, user,**kwargs):
    print("----------------------------------")
    print("loggin successfull!!")
    print("SENDER:", sender)
    print("REQUEST:", request)
    print("USER:", user)
    print(f"Keyword Arguments:{kwargs}")
#user_logged_in.connect(login_success, sender=User)

@receiver(user_logged_out, sender= User)
def logout_success(sender, request, user,**kwargs):
    print("----------------------------------")
    print("logout successfull!!")
    print("SENDER:", sender)
    print("REQUEST:", request)
    print("USER:", user)
    print(f"Keyword Arguments:{kwargs}")
#user_logged_out.connect(logout_success, sender=User)

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("----------------------------------")
    print("Login failed!!")
    print("SENDER:", sender)
    print("CREDENTIALS:",credentials )
    print("REQUEST:", request)
#user_login_failed.connect(login_failed)

@receiver(pre_save, sender= User)  #sender can be model name as well
def at_beginning_save(sender, instance, **kwargs):
    print("----------------------------------")
    print("Pre save signal!")
    print("SENDER:", sender)
    print("INSTANCE:",instance )
    print(f"Keyword arguments:{kwargs}")
#pre_save.connect(at_beginning_save, sender= User)

@receiver(post_save, sender= User)  #sender can be model name as well
def at_ending_save(sender, instance,created, **kwargs):
    if created:
        print("----------------------------------")
        print("Post save signal!")
        print("Created !!")
        print("SENDER:", sender)
        print("INSTANCE:",instance )
        print(f"Keyword arguments:{kwargs}")
    else:
        print("----------------------------------")
        print("Post save signal!")
        print("Updated !!")
        print("SENDER:", sender)
        print("INSTANCE:",instance )
        print(f"Keyword arguments:{kwargs}")
#post_save.connect(at_ending_save, sender= User)

@receiver(pre_delete, sender= User)  #sender can be model name as well
def at_beginning_delete(sender, instance, **kwargs):
    print("----------------------------------")
    print("Pre DELETE!")
    print("SENDER:", sender)
    print("INSTANCE:",instance )
    print(f"Keyword arguments:{kwargs}")
#pre_delete.connect(at_beginning_delete, sender= User)

@receiver(post_delete, sender= User)  #sender can be model name as well
def at_ending_delete(sender, instance, **kwargs):
    print("----------------------------------")
    print("Post DELETE!")
    print("SENDER:", sender)
    print("INSTANCE:",instance )
    print(f"Keyword arguments:{kwargs}")
#post_delete.connect(at_ending_delete, sender= User)

@receiver(pre_init, sender= User)  #sender can be model name as well
def at_begin_init(sender, *args, **kwargs):
    print("----------------------------------")
    print("AT the beggining of init method!")
    print("SENDER:", sender)
    print(f"ARGS:{args}" )
    print(f"Keyword arguments:{kwargs}")
#pre_init.connect(at_begin_init, sender= User)

@receiver(post_init, sender= User)  #sender can be model name as well
def at_end_init(sender, *args, **kwargs):
    print("----------------------------------")
    print("AT the END of init method!")
    print("SENDER:", sender)
    print(f"ARGS:{args}" )
    print(f"Keyword arguments:{kwargs}")
#pre_init.connect(at_end_init, sender= User)

@receiver(request_finished)  
def at_ending_request(sender,**kwargs):
    print("----------------------------------")
    print("At the ending request")
    print("SENDER:", sender)
    print(f"Keyword arguments:{kwargs}")
#request_finished.connect(at_ending_request

@receiver(got_request_exception)  
def at_req_exception(sender, request, **kwargs):
    print("----------------------------------")
    print("At Request exception!!")
    print("SENDER:", sender)
    print("Request", request )
    print(f"Keyword arguments:{kwargs}")
#got_request_exception.connect(at_req_exception)

@receiver(pre_migrate)  
def before_install_app(sender,app_config, verbosity, interactive,using, plan, apps, **kwargs):
    print("----------------------------------")
    print("BEFORE INSTALL APP !!")
    print("SENDER:", sender)
    print("APP_CONFIG:", app_config )
    print("VERBOSITY:", verbosity)
    print("Interactive:", interactive)
    print("USING:", using)
    print("PLAN:", plan)
    print("APPS:", apps)
    print(f"Keyword arguments:{kwargs}")
#pre_migrate.connect(before_install_app)

@receiver(post_migrate)  
def at_end_migrate_flush(sender,app_config, verbosity, interactive,using, plan, apps, **kwargs):
    print("----------------------------------")
    print("At end migrate flush!!")
    print("SENDER:", sender)
    print("APP_CONFIG:", app_config )
    print("VERBOSITY:", verbosity)
    print("Interactive:", interactive)
    print("USING:", using)
    print("PLAN:", plan)
    print("APPS:", apps)
    print(f"Keyword arguments:{kwargs}")
#post_migrate.connect(at_end_migrate_flush)

@receiver(connection_created)  
def connection_db(sender,connection, **kwargs):
    print("----------------------------------")
    print("Initial connection to database!!")
    print("SENDER:", sender)
    print("Connections:", connection)
    print(f"Keyword arguments:{kwargs}")
#connection_created.connect(connection_db)

