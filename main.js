document.addEventListener("DOMContentLoaded", function() {
    // Function to open the settings modal
    function openSettingsModal() {
        var modal = document.getElementById("settingsModal");
        var span = document.getElementsByClassName("close")[0];

        modal.style.display = "block";

        span.onclick = function() {
            modal.style.display = "none";
        }

        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    }

    // Function to show the attendance page
    function showAttendancePage() {
        document.getElementById("dashboard").classList.add("hidden");
        document.getElementById("attendancePage").classList.remove("hidden");
    }
    //Function to show Contact page
    function showContactPage() {
        document.getElementById("dashboard").classList.add("hidden");
        document.getElementById("ContactPage").classList.remove("hidden");
    }

    // Function to go back to the dashboard
    function showDashboard() {
        document.getElementById("attendancePage").classList.add("hidden");
        document.getElementById("dashboard").classList.remove("hidden");
    }

    // Function to close the settings modal
    function closeSettingsModal() {
        var modal = document.getElementById("settingsModal");
        modal.style.display = "none";
    }

    // Event listeners
    document.getElementById("openSettings").addEventListener("click", function(event) {
        event.preventDefault();
        openSettingsModal();
    });
    document.getElementById("fillAttendanceBtn").addEventListener("click", function(event) {
        event.preventDefault();
        showAttendancePage();
    });
    document.getElementById("ContactParentsBtn").addEventListener("click", function(event) {
        event.preventDefault();
        showContactPage();
    });

    document.getElementById("goBackLink").addEventListener("click", function(event) {
        event.preventDefault();
        closeSettingsModal();
    });

    document.getElementById("goBackToDashboard").addEventListener("click", function(event) {
        event.preventDefault();
        showDashboard();
    });
});
