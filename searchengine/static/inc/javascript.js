   ///javascript file///
function delcon() {
    var con=confirm("This action cannot be undone.  Are you sure that you wish to delete this user from the database?");
    if (con==true)
    {
        alert("Deleted!");
     }else
        alert("Not deleted.")
}  ///this will be finished once the Django project is started///
function logoutcon() {
    var con = confirm("Are you sure that you wish to logout from the admin system?");
    if (con == true)
    {
        alert("Logged out!"),
        location.href = "../../static/search.html"
    }else
        alert("Logout aborted.")
}
function authuser() {
    alert ("Only authorized users should attempt to log in to and use this system!!!")
}
function newsearch() {
    alert ("You may now make a new search!")
}
function loadsearch() {
///to be filled in once the Django project is started this will load search from db with onload///
}
function delcon2()
{
    var con=confirm("This action cannot be undone. " +
    "Are you sure that you wish to delete this file from the database?");
    if (con==true)
    {
        alert("Deleted!");
     }else
        alert("Not deleted.")
}
function importnew() {
    alert ("Imported file should be a .txt file.")
}
function searching() {
	alert("Searching...")
}