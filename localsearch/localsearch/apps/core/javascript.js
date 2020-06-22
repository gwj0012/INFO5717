   ///javascript file///
function delcon() {
    var con=confirm("This action cannot be undone.  Are you sure that you wish to delete this user from the database?");
    if (con==true)
    {
        alert("Deleted!");
     }else
        alert("Not deleted.")
}
function logoutcon() {
    var con = confirm("Are you sure that you wish to logout from the admin system?");
    if (con == true)
    {
        alert("Logged out!"),
        location.href = "search.html"
    }else
        alert("Logout aborted.")
}