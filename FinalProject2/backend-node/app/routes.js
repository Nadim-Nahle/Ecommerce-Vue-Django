const express = require("express");
const {
  googleLogin,
  register,
  login,
  googleRegister,

} = require("../controllers/UserController");


const { registerErrors } = require("../middlewares/ErrorsMiddleware");
const router = express.Router();
const auth = require("../middlewares/AuthMiddleware");


// ROUTES

//AUTH ROUTES
router.post("/auth/register", registerErrors, register);
router.post("/auth/register/google", googleRegister);
router.post("/auth/login", login);
router.post("/auth/login/google", googleLogin);







module.exports = router;
