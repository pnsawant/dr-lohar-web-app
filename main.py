
# This is a code for Dr Gaurav Lohar's Web

# Importing packages
from flask import Flask,render_template,request,redirect,session,url_for
from flask_mail import Mail, Message
import json
from flask_sqlalchemy import SQLAlchemy


# Program for getting local datetime in India -
#Importing packages
from datetime import datetime
import pytz
# Setting Indian time zone
IST = pytz.timezone('Asia/Kolkata')
#Getting Indian time
Date_India = datetime.now(IST)
# Specifying format (Format : %Y:%b:%d %H:%M:%S %Z %z )
format = "%d %b %Y | %H:%M"
# Printing time
STD_Date_India = Date_India.strftime(format)
#End

# This function makes google drive share link embeddeble in html for e.g., images
def Link_Converter(old_drive_link):
    try:
        splited_link = old_drive_link.split("/")    # Splits it into a list [...]
        id_part = splited_link[5]      # Access the id part of url
        joining_part = "https://drive.google.com/uc?export=view&id="       # This part makes link embeddeble in html
        link_to_embed = joining_part + id_part       # Joins the id & embeddeble part & gives final link
        return link_to_embed        # Return the final embeddeble link
    except:
        return old_drive_link
#End

# Title to slug converter by Function
def Slug_Maker(Title): #Takes title as argument
    try:
        Splitted_Title = Title.split(" ")  # Splits words apart which have spaces within

        Lower_Case_Title = [items.lower() for items in Splitted_Title]  # Gives list of words in lower case
        
        if Lower_Case_Title[-1]=="": # Checks if there is space at the end

            Lower_Case_Title.pop(-1) # Deletes Space

            Slug = ("-").join(Lower_Case_Title) # Joins words in list with "-" to make a slug

            return Slug # Finally returns slug

        else:

            Slug = ("-").join(Lower_Case_Title)  # Joins words in list with "-" to make a slug

            return Slug # If there is no space returns slug
    
    except:
        return Title # Returns title as it is if there are no spaces in a line
# Slug_Maker End

# Defing app
app=Flask(__name__)


# Accesing config.json file
# with open ("config.json","r") as conf:
#     params = json.load(conf)
with open ("config.json","r") as conf:
    params = json.load(conf)
# Json Section Ended



# Setting secret key
app.secret_key = params["secret_key"]




# Creating Endpoints
@app.route("/")
def home():
    conf_lim = Conferences.query.order_by(Conferences.srno.desc()).limit(6)
    awrd_lim = Awards.query.order_by(Awards.srno.desc()).limit(6)
    pub_lim = Publications.query.order_by(Publications.srno.desc()).limit(6)
    memb_lim = Memberships.query.order_by(Memberships.srno.desc()).limit(6)
    clb = Collaborations.query.all()
    blg_lim = Blog.query.order_by(Blog.srno.desc()).limit(3)
    grp_memb = GroupMembers.query.all()
    prj_lim = Projects.query.order_by(Projects.srno.desc()).limit(6)
    pnt_lim = Patents.query.order_by(Patents.srno.desc()).limit(6)
    awrd_last =  Awards.query.order_by(Awards.srno.desc()).first()
    pnt_last =  Patents.query.order_by(Patents.srno.desc()).first()
    publi_last =  Publications.query.order_by(Publications.srno.desc()).first()
    prj_last =  Projects.query.order_by(Projects.srno.desc()).first()
    wrk_lim = Workshop.query.order_by(Workshop.srno.desc()).limit(6)
    ind_lim = InductionProgram.query.order_by(InductionProgram.srno.desc()).limit(6)
    conforgsec_lim = ConfOrgSec.query.order_by(ConfOrgSec.srno.desc()).limit(6)


    return render_template("index.html",
    conf=conf,
    awrd_lim=awrd_lim,
    pub_lim=pub_lim,
    memb_lim=memb_lim,
    conf_lim=conf_lim,
    clb=clb,
    blg_lim=blg_lim,
    grp_memb=grp_memb,
    prj_lim=prj_lim,
    pnt_lim=pnt_lim,
    awrd_last=awrd_last,
    pnt_last=pnt_last,
    publi_last=publi_last,
    prj_last=prj_last,
    wrk_lim=wrk_lim,
    ind_lim = ind_lim,
    conforgsec_lim = conforgsec_lim,
    params = params
    )

@app.route("/awards")
def awards():
    awd = Awards.query.all()
    memb = Memberships.query.all()
    return render_template("awards.html",awd=awd,memb=memb)


@app.route("/projects")
def projects():
    prj = Projects.query.all()
    return render_template("projects.html",prj=prj)


@app.route("/patents")
def patents():
    pnt = Patents.query.all()
    return render_template("patents.html",pnt=pnt)



@app.route("/publications")
def publications():
    publi = Publications.query.all()
    return render_template("publications.html",publi=publi,params=params)

@app.route("/conferences")
def conferences():
    conf = Conferences.query.all()
    wrk = Workshop.query.all()
    indpro = InductionProgram.query.all()
    conforgsec = ConfOrgSec.query.all()
    return render_template("conferences.html",conf=conf,wrk=wrk,indpro=indpro,conforgsec=conforgsec)


# Blog Stuff

@app.route("/blog")
def blog():
    blg_recent = Blog.query.order_by(Blog.srno.desc()).limit(3)
    blg_p = Blog.query.all()
    blg_three = Blog.query.order_by(Blog.srno.desc()).limit(3)
    return render_template("blog.html",blg_recent=blg_recent,blg_p=blg_p,blg_three=blg_three,params=params)

@app.route("/blog/post/")
def blogpost():
    return redirect(url_for('blog'))

# Rendering blog posts
@app.route("/blog/post/<string:slug>/", methods = ['GET', 'POST'])
def display_blog_post(slug):
    blg_p = Blog.query.filter_by(slug=slug).first()
    blg_recent = Blog.query.order_by(Blog.srno.desc()).limit(8)
    blg_three = Blog.query.order_by(Blog.srno.desc()).limit(3)
    return render_template("blog-post.html",blg_p=blg_p,blg_recent=blg_recent,blg_three=blg_three,params=params)
# Blog stuff ended


# Admin Stuff
# Login Of Admin Section
@app.route("/login", methods=['GET','POST'])
def login():
    if ("user" in session and session["user"]== params["admin_user"]):

        return redirect(url_for('admin'))

    else:
        if (request.method=="POST" and "input_username" in request.form):
            session.pop("user",None)
            username = request.form.get("input_username")
            password= request.form.get("input_password")

            if (username == params["admin_user"] and password == params["admin_password"]):
                session["user"]= username
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('login'))

    return render_template("login.html")
# Login of admin section ended

# Admin logout
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for('login'))
# Admin Stuff Ended

# 404 Page rendering
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Useless Endpoints ! BUT IMPORTANT
# @app.route("/portfolio")
# def portfolio():
#     return render_template("/templates-to-repeat/portfolio-details.html")

# @app.route("/inner")
# def inner():
#     return render_template("/templates-to-repeat/inner-page.html")


# Endpoint section ended



# Connecting to database
localhost = params["localhost_True_Or_False"]

if localhost=="True":
    app.config['SQLALCHEMY_DATABASE_URI'] = params["localhost_uri"]    #Fist Database
    app.config['SQLALCHEMY_BINDS'] = {'blog':params["localhost_bind_blog_uri"]}  #Second Database
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["pythonanywhere_uri"]    #Fist Database
    app.config['SQLALCHEMY_BINDS'] = {'blog':params["pythonanywhere_bind_blog_uri"]}  #Second Database

db = SQLAlchemy(app)
# Database connect section ended

# Using Database
class Publications(db.Model):
    __tablename__ = "Publications"
    srno = db.Column(db.Integer, primary_key=True, nullable=False)
    reference = db.Column(db.String(500), nullable=True)
    doi = db.Column(db.String(500), nullable=True)
    year = db.Column(db.Integer, nullable=True)

class Contacts(db.Model):
    __tablename__ = "Contacts"
    name = db.Column(db.String(500), primary_key=True, nullable=False)
    email = db.Column(db.String(500), nullable=False)
    subject = db.Column(db.String(500), nullable=False)
    message = db.Column(db.String(2000), nullable=False)
    info = db.Column(db.String(500), nullable =False)

class Conferences(db.Model):
    __tablename__ = "Conferences"
    srno = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(500), nullable=True)
    place = db.Column(db.String(500), nullable=True)
    year = db.Column(db.Integer, nullable=True)


class Workshop(db.Model):
    __tablename__ = "Workshop"
    srno = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(500), nullable=True)
    place = db.Column(db.String(500), nullable=True)
    year = db.Column(db.Integer, nullable=True)

class InductionProgram(db.Model):
    __tablename__ = "InductionProgram"
    srno = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(500), nullable=True)
    place = db.Column(db.String(500), nullable=True)
    year = db.Column(db.Integer, nullable=True)

class ConfOrgSec(db.Model):
    __tablename__ = "ConfOrgSec"
    srno = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(500), nullable=True)
    role = db.Column(db.String(500), nullable=True)
    place = db.Column(db.String(500), nullable=True)
    year = db.Column(db.Integer, nullable=True)


class Awards(db.Model):
    __tablename__ = "Awards"
    srno = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(500), nullable=True)
    subtitle = db.Column(db.String(500), nullable=True)
    imagelink = db.Column(db.String(500), nullable=True)

class Memberships(db.Model):
    __tablename__ = "Memberships"
    srno = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(500), nullable=True)
    subtitle = db.Column(db.String(500), nullable=True)

class GroupMembers(db.Model):
    __tablename__ = "GroupMembers"
    srno = db.Column(db.Integer, primary_key=True, nullable=False)
    firstname = db.Column(db.String(500), nullable=True)
    surname = db.Column(db.String(500), nullable=True)
    imagelink = db.Column(db.String(500), nullable=True)
    role = db.Column(db.String(500), nullable=True)
    info = db.Column(db.String(2000), nullable=True)

class Collaborations(db.Model):
    __tablename__ = "Collaborations"
    srno = db.Column(db.Integer, primary_key=True, nullable=False)
    firstname = db.Column(db.String(500), nullable=True)
    surname = db.Column(db.String(500), nullable=True)
    place = db.Column(db.String(500), nullable=True)
    aboutlink = db.Column(db.String(500), nullable=True)

class Patents(db.Model):
    __tablename__ = "Patents"
    srno = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(500), nullable=True)
    subtitle = db.Column(db.String(500), nullable=True)
    imagelink = db.Column(db.String(500), nullable=True)
    para1 = db.Column(db.String(1000), nullable=True)
    line1 = db.Column(db.String(500), nullable=True)
    line2 = db.Column(db.String(500), nullable=True)
    line3 = db.Column(db.String(500), nullable=True)
    line4 = db.Column(db.String(500), nullable=True)
    para2 = db.Column(db.String(1000), nullable=True)

class Projects(db.Model):
    __tablename__ = "Projects"
    srno = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(500), nullable=True)
    subtitle = db.Column(db.String(500), nullable=True)
    imagelink = db.Column(db.String(500), nullable=True)
    para1 = db.Column(db.String(1000), nullable=True)
    line1 = db.Column(db.String(500), nullable=True)
    line2 = db.Column(db.String(500), nullable=True)
    line3 = db.Column(db.String(500), nullable=True)
    line4 = db.Column(db.String(500), nullable=True)
    para2 = db.Column(db.String(1000), nullable=True)


class Blog(db.Model):
    __bind_key__ = "blog"
    __tablename__ = "Blog"
    srno = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(500), nullable=False)
    subtitle = db.Column(db.String(500), nullable=True)
    slug = db.Column(db.String(500), nullable=False)
    info = db.Column(db.String(50), nullable=False)
    intro = db.Column(db.String(2500), nullable=True)
    featuredimglink = db.Column(db.String(100), nullable=True)
    tag1 = db.Column(db.String(50), nullable=True)
    tag2 = db.Column(db.String(50), nullable=True)
    tag3 = db.Column(db.String(50), nullable=True)
    content1 = db.Column(db.String(5000), nullable=True)
    imglink1 = db.Column(db.String(100), nullable=True)
    content2 = db.Column(db.String(5000), nullable=True)
    imglink2 = db.Column(db.String(100), nullable=True)
    extlink = db.Column(db.String(100), nullable=True)
    content3 = db.Column(db.String(5000), nullable=True)
    imglink3 = db.Column(db.String(100), nullable=True)
    content4 = db.Column(db.String(5000), nullable=True)
    imglink4 = db.Column(db.String(100), nullable=True)



@app.route("/admin",methods=["GET","POST"])
def admin():
    if ("user" in session and session["user"]== params["admin_user"]):
        if (request.method=="GET"):
            conf = Conferences.query.all()
            publi = Publications.query.all()
            cont = Contacts.query.all()
            awrd = Awards.query.all()
            memb = Memberships.query.all()
            grp_memb = GroupMembers.query.all()
            clb = Collaborations.query.all()
            pnt = Patents.query.all()
            prj = Projects.query.all()
            blg = Blog.query.all()
            wrk = Workshop.query.all()
            publi_last =  Publications.query.order_by(Publications.srno.desc()).first()
            blg_post_last =  Blog.query.order_by(Blog.srno.desc()).first()
            cont_last =  Contacts.query.order_by(Contacts.name.desc()).first()
            indpro = InductionProgram.query.all()
            conforgsec = ConfOrgSec.query.all()

            return render_template("admin.html", publi=publi, conf=conf,cont=cont,awrd=awrd,memb=memb,grp_memb=grp_memb,clb=clb,pnt=pnt,prj=prj,blg=blg,
                publi_last=publi_last,
                blg_post_last=blg_post_last,
                cont_last=cont_last,
                wrk=wrk,
                indpro=indpro,
                conforgsec = conforgsec,
                params=params
            )

        # Publication add New entry to database
        if (request.method=="POST" and "publi_reference" in request.form):
            publi_srno = request.form.get("publi_srno")
            publi_reference =request.form.get("publi_reference")
            publi_doi=request.form.get("publi_doi")
            publi_year =request.form.get("publi_year")

            entry = Publications(srno=publi_srno,reference=publi_reference,doi=publi_doi,year=publi_year)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('admin'))


        # Conferences add New entry to database
        if (request.method=="POST" and "conf_place" in request.form):
            conf_srno = request.form.get("conf_srno")
            conf_name =request.form.get("conf_name")
            conf_place=request.form.get("conf_place")
            conf_year =request.form.get("conf_year")

            entry = Conferences(srno=conf_srno,name=conf_name,place=conf_place,year=conf_year)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('admin'))


        # Workshop add New entry to database
        if (request.method=="POST" and "wrk_place" in request.form):
            wrk_srno = request.form.get("wrk_srno")
            wrk_name =request.form.get("wrk_name")
            wrk_place=request.form.get("wrk_place")
            wrk_year =request.form.get("wrk_year")

            entry = Workshop(srno=wrk_srno,name=wrk_name,place=wrk_place,year=wrk_year)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('admin'))

        # InductionProgram add New entry to database
        if (request.method=="POST" and "indpro_place" in request.form):
            indpro_srno = request.form.get("indpro_srno")
            indpro_name =request.form.get("indpro_name")
            indpro_place=request.form.get("indpro_place")
            indpro_year =request.form.get("indpro_year")

            entry = InductionProgram(srno=indpro_srno,name=indpro_name,place=indpro_place,year=indpro_year)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('admin'))

        # Conf Org Sec add New entry to database
        if (request.method=="POST" and "conforgsec_place" in request.form):
            conforgsec_srno = request.form.get("conforgsec_srno")
            conforgsec_name =request.form.get("conforgsec_name")
            conforgsec_role =request.form.get("conforgsec_role")
            conforgsec_place=request.form.get("conforgsec_place")
            conforgsec_year =request.form.get("conforgsec_year")

            entry = ConfOrgSec(srno=conforgsec_srno,name=conforgsec_name,role=conforgsec_role,place=conforgsec_place,year=conforgsec_year)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('admin'))

        # Awards Add New Entry to database
        if (request.method=="POST" and "award_info" in request.form):
            award_srno = request.form.get("award_srno")
            award_title =request.form.get("award_title")
            award_subt =request.form.get("award_subt")
            award_imglink =request.form.get("award_imglink")

            award_imglink_final  = Link_Converter(award_imglink)

            entry = Awards(srno=award_srno,title=award_title,subtitle=award_subt,imagelink=award_imglink_final)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('admin'))


        # Memberships Add New Entry to database
        if (request.method=="POST" and "membership_info" in request.form):
            memb_srno = request.form.get("membership_srno")
            memb_title =request.form.get("membership_title")
            memb_subt =request.form.get("membership_subt")

            entry = Memberships(srno=memb_srno,title=memb_title,subtitle=memb_subt)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('admin'))


        # Group Members Add New Entry to database
        if (request.method=="POST" and "grp_memb_info" in request.form):
            grp_memb_srno = request.form.get("grp_memb_srno")
            grp_memb_firstname =request.form.get("grp_memb_firstname")
            grp_memb_surname =request.form.get("grp_memb_surname")
            grp_memb_imglink =request.form.get("grp_memb_imglink")
            grp_memb_role = request.form.get("grp_memb_role")
            grp_memb_info =request.form.get("grp_memb_info")

            grp_memb_imglink_final= Link_Converter(grp_memb_imglink)

            entry = GroupMembers(srno=grp_memb_srno,firstname=grp_memb_firstname,surname=grp_memb_surname,imagelink=grp_memb_imglink_final,role=grp_memb_role,info=grp_memb_info)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('admin'))

        # Collaborations Add New Entry to database
        if (request.method=="POST" and "clb_place" in request.form):
            clb_srno = request.form.get("clb_srno")
            clb_firstname =request.form.get("clb_firstname")
            clb_surname =request.form.get("clb_surname")
            clb_place = request.form.get("clb_place")
            clb_aboutlink =request.form.get("clb_aboutlink")


            entry = Collaborations(srno=clb_srno,firstname=clb_firstname,surname=clb_surname,place=clb_place,aboutlink=clb_aboutlink)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('admin'))


        # Patents Add New Entry to database
        if (request.method=="POST" and "pnt_subtl" in request.form):
            pnt_srno = request.form.get("pnt_srno")
            pnt_title =request.form.get("pnt_title")
            pnt_subtl =request.form.get("pnt_subtl")
            pnt_imglink =request.form.get("pnt_imglink")
            pnt_para1 = request.form.get("pnt_para1")
            pnt_line1 =request.form.get("pnt_line1")
            pnt_line2 =request.form.get("pnt_line2")
            pnt_line3 =request.form.get("pnt_line3")
            pnt_line4 =request.form.get("pnt_line4")
            pnt_para2 =request.form.get("pnt_para2")

            pnt_imglink_final = Link_Converter(pnt_imglink)

            entry = Patents(srno=pnt_srno,title=pnt_title,subtitle=pnt_subtl,imagelink=pnt_imglink_final,para1=pnt_para1,line1=pnt_line1,line2=pnt_line2,line3=pnt_line3,line4=pnt_line4,para2=pnt_para2)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('admin'))


        # Projects Add New Entry to database
        if (request.method=="POST" and "prj_srno" in request.form):
            prj_srno = request.form.get("prj_srno")
            prj_title =request.form.get("prj_title")
            prj_subtl =request.form.get("prj_subtl")
            prj_imglink =request.form.get("prj_imglink")
            prj_para1 = request.form.get("prj_para1")
            prj_line1 =request.form.get("prj_line1")
            prj_line2 =request.form.get("prj_line2")
            prj_line3 =request.form.get("prj_line3")
            prj_line4 =request.form.get("prj_line4")
            prj_para2 =request.form.get("prj_para2")

            prj_imglink_final = Link_Converter(prj_imglink)

            entry = Projects(srno=prj_srno,title=prj_title,subtitle=prj_subtl,imagelink=prj_imglink_final,para1=prj_para1,line1=prj_line1,line2=prj_line2,line3=prj_line3,line4=prj_line4,para2=prj_para2)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('admin'))

        # Blog Add new entry
        if (request.method=="POST" and "post_srno" in request.form):
            # Getting Data from form
            post_srno = request.form.get("post_srno")
            post_title =request.form.get("post_title")
            post_subtl =request.form.get("post_subtl")
            featured_imglink =request.form.get("featured_imglink")
            tag_1 = request.form.get("tag_1")
            tag_2 =request.form.get("tag_2")
            tag_3 =request.form.get("tag_3")
            post_intro =request.form.get("post_intro")
            content_para_1 =request.form.get("content_para_1")
            content_para_2 =request.form.get("content_para_2")
            content_para_3 =request.form.get("content_para_3")
            content_para_4 =request.form.get("content_para_4")
            post_link_1 =request.form.get("post_link_1")
            post_link_2 =request.form.get("post_link_2")
            post_link_3 =request.form.get("post_link_3")
            post_link_4 =request.form.get("post_link_4")
            post_external_link =request.form.get("post_external_link")

            # Processing Data
            post_slug = Slug_Maker(post_title)      #declared in the top
            post_info = STD_Date_India              #declared in the top
            featured_imglink_final = Link_Converter(featured_imglink)
            post_link_1_final = Link_Converter(post_link_1)
            post_link_2_final = Link_Converter(post_link_2)
            post_link_3_final = Link_Converter(post_link_3)
            post_link_4_final = Link_Converter(post_link_4)

            entry = Blog(
                            srno = post_srno,
                            title = post_title,
                            subtitle = post_subtl,
                            slug = post_slug,
                            info = post_info,
                            intro = post_intro,
                            featuredimglink = featured_imglink_final,
                            tag1 = tag_1,
                            tag2 = tag_2,
                            tag3 = tag_3,
                            content1 = content_para_1,
                            imglink1 = post_link_1_final,
                            content2 = content_para_2,
                            imglink2 = post_link_2_final,
                            extlink = post_external_link,
                            content3 = content_para_3,
                            imglink3 = post_link_3_final,
                            content4 = content_para_4,
                            imglink4 = post_link_4_final
                        )
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))



# Updating Data
#Updating Publications
@app.route("/edit_publi/<string:srno>/", methods = ['GET', 'POST'])
def edit_publi(srno):
    if ("user" in session and session["user"]== params["admin_user"]):

        if (request.method=="POST" and "edit_publi_reference" in request.form):

            # Fetching from Edit modal
            upd_srno = request.form.get("edit_publi_srno")
            upd_reference =request.form.get("edit_publi_reference")
            upd_doi=request.form.get("edit_publi_doi")
            upd_year =request.form.get("edit_publi_year")

            # Fetching from db
            data = Publications.query.filter_by(srno=srno).first()
            data.srno = upd_srno
            data.reference = upd_reference
            data.doi = upd_doi
            data.year= upd_year
            db.session.commit()

            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

# Updating Conferences
@app.route("/edit_conf/<string:srno>/", methods = ['GET', 'POST'])
def edit_conf(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        if (request.method=="POST" and "edit_conf_place" in request.form):

            # Fetching from Edit modal
            upd_srno = request.form.get("edit_conf_srno")
            upd_name =request.form.get("edit_conf_name")
            upd_place=request.form.get("edit_conf_place")
            upd_year =request.form.get("edit_conf_year")

            # Fetching from db
            data = Conferences.query.filter_by(srno=srno).first()
            data.srno = upd_srno
            data.name = upd_name
            data.place = upd_place
            data.year= upd_year
            db.session.commit()

            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))


# Updating Workshop
@app.route("/edit_wrk/<string:srno>/", methods = ['GET', 'POST'])
def edit_wrk(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        if (request.method=="POST" and "edit_wrk_place" in request.form):

            # Fetching from Edit modal
            upd_srno = request.form.get("edit_wrk_srno")
            upd_name =request.form.get("edit_wrk_name")
            upd_place=request.form.get("edit_wrk_place")
            upd_year =request.form.get("edit_wrk_year")

            # Fetching from db
            data = Workshop.query.filter_by(srno=srno).first()
            data.srno = upd_srno
            data.name = upd_name
            data.place = upd_place
            data.year= upd_year
            db.session.commit()

            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))


# Updating InductionProgram
@app.route("/edit_indpro/<string:srno>/", methods = ['GET', 'POST'])
def edit_indpro(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        if (request.method=="POST" and "edit_indpro_place" in request.form):

            # Fetching from Edit modal
            upd_srno = request.form.get("edit_indpro_srno")
            upd_name =request.form.get("edit_indpro_name")
            upd_place=request.form.get("edit_indpro_place")
            upd_year =request.form.get("edit_indpro_year")

            # Fetching from db
            data = InductionProgram.query.filter_by(srno=srno).first()
            data.srno = upd_srno
            data.name = upd_name
            data.place = upd_place
            data.year= upd_year
            db.session.commit()

            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

# Updating ConfOrgSec
@app.route("/edit_conforgsec/<string:srno>/", methods = ['GET', 'POST'])
def edit_conforgsec(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        if (request.method=="POST" and "edit_conforgsec_place" in request.form):

            # Fetching from Edit modal
            upd_srno = request.form.get("edit_conforgsec_srno")
            upd_name =request.form.get("edit_conforgsec_name")
            upd_role=request.form.get("edit_conforgsec_role")
            upd_place=request.form.get("edit_conforgsec_place")
            upd_year =request.form.get("edit_conforgsec_year")

            # Fetching from db
            data = ConfOrgSec.query.filter_by(srno=srno).first()
            data.srno = upd_srno
            data.name = upd_name
            data.role = upd_role
            data.place = upd_place
            data.year= upd_year
            db.session.commit()

            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))


# Updating Awards
@app.route("/edit_awrd/<string:srno>/", methods = ['GET', 'POST'])
def edit_awrd(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        if (request.method=="POST" and "edit_awrd_subtl" in request.form):

            # Fetching from Edit modal
            upd_srno = request.form.get("edit_awrd_srno")
            upd_title =request.form.get("edit_awrd_title")
            upd_subtl =request.form.get("edit_awrd_subtl")
            upd_imglink =request.form.get("edit_awrd_imglink")

            upd_imglink_final = Link_Converter(upd_imglink)

            # Fetching from db
            data = Awards.query.filter_by(srno=srno).first()
            data.srno = upd_srno
            data.title = upd_title
            data.subtitle = upd_subtl
            data.imagelink =  upd_imglink_final
            db.session.commit()

            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))


# Updating Memberships
@app.route("/edit_memb/<string:srno>/", methods = ['GET', 'POST'])
def edit_memb(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        if (request.method=="POST" and "edit_memb_subtl" in request.form):

            # Fetching from Edit modal
            upd_srno = request.form.get("edit_memb_srno")
            upd_title =request.form.get("edit_memb_title")
            upd_subtl =request.form.get("edit_memb_subtl")

            # Fetching from db
            data = Memberships.query.filter_by(srno=srno).first()
            data.srno = upd_srno
            data.title = upd_title
            data.subtitle = upd_subtl
            db.session.commit()

            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

# Updating GroupMembers
@app.route("/edit_grp_memb/<string:srno>/", methods = ['GET', 'POST'])
def edit_grp_memb(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        if (request.method=="POST" and "edit_grp_memb_role" in request.form):

            # Fetching from Edit modal
            upd_srno = request.form.get("edit_grp_memb_srno")
            upd_firstname =request.form.get("edit_grp_memb_firstname")
            upd_surname =request.form.get("edit_grp_memb_surname")
            upd_imglink = request.form.get("edit_grp_memb_imglink")
            upd_role = request.form.get("edit_grp_memb_role")
            upd_info =request.form.get("edit_grp_memb_info")

            upd_imglink_final = Link_Converter(upd_imglink)

            # Fetching from db
            data = GroupMembers.query.filter_by(srno=srno).first()
            data.srno = upd_srno
            data.firstname = upd_firstname
            data.surname = upd_surname
            data.imagelink= upd_imglink_final
            data.role = upd_role
            data.info = upd_info
            db.session.commit()

            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

# Updating Collaborations
@app.route("/edit_clb/<string:srno>/", methods = ['GET', 'POST'])
def edit_clb(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        if (request.method=="POST" and "edit_clb_place" in request.form):

            # Fetching from Edit modal
            upd_srno = request.form.get("edit_clb_srno")
            upd_firstname =request.form.get("edit_clb_firstname")
            upd_surname =request.form.get("edit_clb_surname")
            upd_place = request.form.get("edit_clb_place")
            upd_aboutlink = request.form.get("edit_clb_aboutlink")


            # Fetching from db
            data = Collaborations.query.filter_by(srno=srno).first()
            data.srno = upd_srno
            data.firstname = upd_firstname
            data.surname = upd_surname
            data.place = upd_place
            data.aboutlink = upd_aboutlink
            db.session.commit()

            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))


# Updating Patents
@app.route("/edit_pnt/<string:srno>/", methods = ['GET', 'POST'])
def edit_pnt(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        if (request.method=="POST" and "edit_pnt_subtl" in request.form):

            # Fetching from Edit modal
            upd_srno = request.form.get("edit_pnt_srno")
            upd_title =request.form.get("edit_pnt_title")
            upd_subtl =request.form.get("edit_pnt_subtl")
            upd_imglink = request.form.get("edit_pnt_imglink")
            upd_para1 = request.form.get("edit_pnt_para1")
            upd_line1 = request.form.get("edit_pnt_line1")
            upd_line2 = request.form.get("edit_pnt_line2")
            upd_line3 = request.form.get("edit_pnt_line3")
            upd_line4 = request.form.get("edit_pnt_line4")
            upd_para2= request.form.get("edit_pnt_para2")

            upd_imglink_final = Link_Converter(upd_imglink)

            # Fetching from db
            data = Patents.query.filter_by(srno=srno).first()
            data.srno = upd_srno
            data.title = upd_title
            data.subtitle = upd_subtl
            data.imagelink= upd_imglink_final
            data.para1 = upd_para1
            data.line1 = upd_line1
            data.line2 = upd_line2
            data.line3 = upd_line3
            data.line4 = upd_line4
            data.para2 = upd_para2
            db.session.commit()

            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

# Updating Projects
@app.route("/edit_prj/<string:srno>/", methods = ['GET', 'POST'])
def edit_prj(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        if (request.method=="POST" and "edit_prj_subtl" in request.form):

            # Fetching from Edit modal
            upd_srno = request.form.get("edit_prj_srno")
            upd_title =request.form.get("edit_prj_title")
            upd_subtl =request.form.get("edit_prj_subtl")
            upd_imglink = request.form.get("edit_prj_imglink")
            upd_para1 = request.form.get("edit_prj_para1")
            upd_line1 = request.form.get("edit_prj_line1")
            upd_line2 = request.form.get("edit_prj_line2")
            upd_line3 = request.form.get("edit_prj_line3")
            upd_line4 = request.form.get("edit_prj_line4")
            upd_para2= request.form.get("edit_prj_para2")

            upd_imglink_final = Link_Converter(upd_imglink)

            # Fetching from db
            data = Projects.query.filter_by(srno=srno).first()
            data.srno = upd_srno
            data.title = upd_title
            data.subtitle = upd_subtl
            data.imagelink= upd_imglink_final
            data.para1 = upd_para1
            data.line1 = upd_line1
            data.line2 = upd_line2
            data.line3 = upd_line3
            data.line4 = upd_line4
            data.para2 = upd_para2
            db.session.commit()

            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

# Updating Blog Post
@app.route("/edit_blg/<string:srno>/", methods = ['GET', 'POST'])
def edit_blg(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        if (request.method=="POST" and "edit_post_subtl" in request.form):

            # Fetching from Edit modal
            upd_srno = request.form.get("edit_post_srno")
            upd_title =request.form.get("edit_post_title")
            upd_subtl =request.form.get("edit_post_subtl")
            upd_featured_imglink =request.form.get("edit_featured_imglink")
            upd_tag1 = request.form.get("edit_tag_1")
            upd_tag2 =request.form.get("edit_tag_2")
            upd_tag3 =request.form.get("edit_tag_3")
            upd_intro =request.form.get("edit_post_intro")
            upd_content1 =request.form.get("edit_content_para_1")
            upd_content2 =request.form.get("edit_content_para_2")
            upd_content3 =request.form.get("edit_content_para_3")
            upd_content4 =request.form.get("edit_content_para_4")
            upd_post_link_1 =request.form.get("edit_post_link_1")
            upd_post_link_2 =request.form.get("edit_post_link_2")
            upd_post_link_3 =request.form.get("edit_post_link_3")
            upd_post_link_4 =request.form.get("edit_post_link_4")
            upd_post_external_link =request.form.get("edit_post_external_link")

        # Processing Data
            upd_slug = Slug_Maker(upd_title)      #declared in the top
            upd_info = STD_Date_India              #declared in the top
            upd_featured_imglink_final = Link_Converter(upd_featured_imglink)
            upd_post_link_1_final = Link_Converter(upd_post_link_1)
            upd_post_link_2_final = Link_Converter(upd_post_link_2)
            upd_post_link_3_final = Link_Converter(upd_post_link_3)
            upd_post_link_4_final = Link_Converter(upd_post_link_4)


        # Fetching from db & updating
            data = Blog.query.filter_by(srno=srno).first()
            data.srno = upd_srno
            data.title = upd_title
            data.subtitle = upd_subtl
            data.slug = upd_slug
            data.info = upd_info
            data.intro = upd_intro
            data.featuredimglink= upd_featured_imglink_final
            data.tag1 = upd_tag1
            data.tag2 = upd_tag2
            data.tag3 = upd_tag3
            data.content1 = upd_content1
            data.imglink1 = upd_post_link_1_final
            data.content2 = upd_content2
            data.imglink2 = upd_post_link_2_final
            data.extlink = upd_post_external_link
            data.content3 = upd_content3
            data.imglink3 = upd_post_link_3_final
            data.content4 = upd_content4
            data.imglink4 = upd_post_link_4_final
            db.session.commit()

            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))
# Updating section ended


# Deleting the data
# Deleting Publiactions
@app.route('/delete_publi/<string:srno>/', methods = ['GET', 'POST'])
def delete_publi(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        my_data = Publications.query.filter_by(srno=srno).first()
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

#Deleting conferences
@app.route('/delete_conf/<string:srno>/', methods = ['GET', 'POST'])
def delete_conf(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        my_data = Conferences.query.filter_by(srno=srno).first()
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))


#Deleting Workshop
@app.route('/delete_wrk/<string:srno>/', methods = ['GET', 'POST'])
def delete_wrk(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        my_data = Workshop.query.filter_by(srno=srno).first()
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

#Deleting InductionProgram
@app.route('/delete_indpro/<string:srno>/', methods = ['GET', 'POST'])
def delete_indpro(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        my_data = InductionProgram.query.filter_by(srno=srno).first()
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

#Deleting ConfOrgSec
@app.route('/delete_conforgsec/<string:srno>/', methods = ['GET', 'POST'])
def delete_conforgsec(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        my_data = ConfOrgSec.query.filter_by(srno=srno).first()
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))


# Deleting Award
@app.route('/delete_awards/<string:srno>/', methods = ['GET', 'POST'])
def delete_awards(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        my_data = Awards.query.filter_by(srno=srno).first()
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

# Deleting Memberships
@app.route('/delete_memberships/<string:srno>/', methods = ['GET', 'POST'])
def delete_memberships(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        my_data = Memberships.query.filter_by(srno=srno).first()
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

# Deleting Group Members
@app.route('/delete_grp_memb/<string:srno>/', methods = ['GET', 'POST'])
def delete_grp_memb(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        my_data = GroupMembers.query.filter_by(srno=srno).first()
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

# Deleting Collaborations
@app.route('/delete_clb/<string:srno>/', methods = ['GET', 'POST'])
def delete_clb(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        my_data = Collaborations.query.filter_by(srno=srno).first()
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

# Deleting Patents
@app.route('/delete_pnt/<string:srno>/', methods = ['GET', 'POST'])
def delete_pnt(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        my_data = Patents.query.filter_by(srno=srno).first()
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

# Deleting Projects
@app.route('/delete_prj/<string:srno>/', methods = ['GET', 'POST'])
def delete_prj(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        my_data = Projects.query.filter_by(srno=srno).first()
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

# Deleting Blog Post
@app.route('/delete_blg/<string:srno>/', methods = ['GET', 'POST'])
def delete_blg(srno):
    if ("user" in session and session["user"]== params["admin_user"]):
        my_data = Blog.query.filter_by(srno=srno).first()
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

# Deleting Contact Post
@app.route('/delete_cont/<string:name>/', methods = ['GET', 'POST'])
def delete_cont(name):
    if ("user" in session and session["user"]== params["admin_user"]):
        my_data = Contacts.query.filter_by(name=name).first()
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))
#Deleting data ended




#Configuring for email
app.config.update(dict(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = params["my_gmail_id"],
    MAIL_PASSWORD = params["gmail_password"]
))

mail = Mail(app)

@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method =="POST":
        try:
            cont_name = request.form.get("cnt_name")
            cont_email = request.form.get("cnt_email")
            cont_subject = request.form.get("cnt_subject")
            cont_message = request.form.get("cnt_message")
            cont_date = STD_Date_India #Configured top in the code

            # Sending mails from contact form
            msg=Message(subject=f"Web contact message from {cont_name}",
            body=f" Name : {cont_name}\n Email : {cont_email}\n Subject : {cont_subject}\n Message : {cont_message}\n Sent On : {cont_date}",
            sender=f"{cont_email}",
            recipients=["drgauravlohar@gmail.com"])
            mail.send(msg)
            # Mail sending Section Ended

            # Adding Entry in db
            entry = Contacts(name=cont_name, email=cont_email,subject=cont_subject,message=cont_message,info=cont_date)
            db.session.add(entry)
            db.session.commit()
            # Entry in db ended
            return "I got your message!"
        except:
            try:
                # Sending mails from contact form
                msg=Message(subject=f"Web contact message from {cont_name}",
                body=f" Name : {cont_name}\n Email : {cont_email}\n Subject : {cont_subject}\n Message : {cont_message}\n Sent On : {cont_date}",
                sender=f"{cont_email}",
                recipients=["drgauravlohar@gmail.com"])
                mail.send(msg)
                # Mail sending Section Ended
                return "I got your message!"
            except:
                # Adding Entry in db
                entry = Contacts(name=cont_name, email=cont_email,subject=cont_subject,message=cont_message,info=cont_date)
                db.session.add(entry)
                db.session.commit()
                # Entry in db ended
                return "I got your message!"
        else:
            return "Error in getting your message!!"
# Using Database section ended


# Running app
if params["app_debug_value"]=="True":
    params["app_debug_value"]=bool("True")  # Debug = True
else:
    params["app_debug_value"]=bool("")  # Debug = False

if __name__ == '__main__':
    app.run(debug=params["app_debug_value"])
# Running app section ended




# Extra Notes

# {{ ''.join(['', pub_lim.doi]) }}

# {{ ''.join(['', pnt_lim.imagelink]) }}


# {%if params["localhost_True_Or_False"]=="True"%}
# {%else%}
# {%endif%}

# Notes Ended
