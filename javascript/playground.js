function adminActions(func) {
  return func;
}

buttons = () => {
  return "<button>Admin Dashboard</button>";
};

try {
  console.log(adminActions(buttons));
} catch (error) {
  console.log("No admin is logged in", error);
}
