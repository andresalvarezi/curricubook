document.addEventListener('DOMContentLoaded', function() {
    console.info("Created with CurricuBook!");

    M.Sidenav.init(document.querySelectorAll('.sidenav'), {});
    M.Modal.init(document.querySelectorAll('.modal'), {});
    M.FloatingActionButton.init(document.querySelectorAll('.fixed-action-btn'), {});
});
