// Pass JavaScript Objects as Function Arguments by Leveraging Deconstruction

const User = {
  name: "Kristine",
  email: "kristine@devcamp.com",
};

const renderUser = ({ name, email }) => {
  console.log(`${name}: ${email}`);
};

class User{
    constructor(username, status) {
        this.username = username;
        this.status = status;
    }

    loginEvent() {
        this.status = 'active';
        return `${this.username} is active`;
    }
}

const user = new User('your_username', 'away');

console.log(user.loginEvent());
console.log(user.loginEvent())