const { addUser, getByEmail, addGoogleUser } = require("../services/UserService");
const User = require("../models/user")
const { all } = require('../app/routes')
require("dotenv").config();
const bcrypt = require(`bcryptjs`);
const jwt = require('jsonwebtoken');
const TOKEN_SECRET = process.env.TOKEN_SECRET;
const { validationResult } = require("express-validator/check");

//REGISTER CONTROLLER
async function register(req, res) {
  try {
    //VALIDATING NAME,EMAIL,PASSWORD
    const errors = validationResult(req);

    if (!errors.isEmpty()) {

      return res.status(422).jsonp(errors);

    } else {

      //ENCRYPT THE PASSWORD
      const salt = await bcrypt.genSalt(10);
      const hashPassword = await bcrypt.hash(req.body.password, salt);

      //STORE THE NEW USER
      const addUserResult = await addUser(req.body, hashPassword);
      return res.send({ userId: addUserResult._id });
    }
    //CATCHING ERRORS
  } catch (error) {

    res.status(409).send(error);

  }
}
//GOOGLE REGISTER CONTROLLER
async function googleRegister(req, res) {
  try {
    //ENCRYPT THE PASSWORD
    const salt = await bcrypt.genSalt(10);
    const hashPassword = await bcrypt.hash(req.body.email + TOKEN_SECRET, salt);

    //STORE THE NEW USER
    const addUserResult = await addGoogleUser(req.body, hashPassword);
    return res.send({ userId: addUserResult._id });
    //CATCHING ERRORS
  } catch (error) {

    res.status(409).send(error);

  }
}


//LOGIN CONTROLLER
async function login(req, res) {
  try {

    const user = await getByEmail(req.body.email);
    if (!user) return res.status(401).send('invalid email');

    const validPassword = await bcrypt.compare(req.body.password, user.password);
    if (!validPassword) return res.status(400).send('invalid password');

    //CRETAE USER AND JWT TOKEN
    const token = jwt.sign(
      { _id: user._id, name: user.name, email: user.email },
      TOKEN_SECRET

    );

    return res.send({
      user: {
        name: user.name,
        email: user.email, _id: user._id,
        roles: user.roles,
        username: user.username,
        followings: user.followings
      },
      secret_token: token,
      url: user.url
    },
    );

    //CATCHING ERRORS
  } catch (error) {

    //console.log(error);
    res.status(500).send(error);

  }
}

//ADMIN LOGIN
async function adminLogin(req, res) {
  const email = 'admin@gmail.com';
  try {
    const user = await getByEmail(email);
    const token = jwt.sign(
      { _id: user._id, name: user.name, email: user.email },
      TOKEN_SECRET

    );

    return res.send({
      user: {
        name: user.name,
        email: user.email, _id: user._id,
        roles: user.roles,
        username: user.username,
        followings: user.followings
      },
      secret_token: token,
      url: user.url
    },
    );

  } catch (error) {
    res.status(400).send('error');
  }
}
//GOOGLE LOGIN CONTROLLER
async function googleLogin(req, res) {
  try {

    const user = await getByEmail(req.body.email);
    if (!user) return res.status(401).send('invalid email');

    const validPassword = await bcrypt.compare(req.body.email + TOKEN_SECRET, user.password);
    if (!validPassword) return res.status(400).send('invalid password');

    //CRETAE USER AND JWT TOKEN
    const token = jwt.sign(
      { _id: user._id, name: user.name, email: user.email },
      TOKEN_SECRET

    );

    return res.send({
      user: {
        name: user.name,
        email: user.email,
        _id: user._id,
        roles: user.roles,
        username: user.username,
        followings: user.followings
      },
      secret_token: token,
      url: user.url
    });

    //CATCHING ERRORS
  } catch (error) {

    //console.log(error);
    res.status(500).send(error);

  }
}







//EXPORTING MODULES
module.exports = {
  register,
  login,
  googleRegister,
  googleLogin,

};