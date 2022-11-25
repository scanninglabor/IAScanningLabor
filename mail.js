
const nodemailer = require("nodemailer");

transporter=nodemailer.createTransport({
    host: "smtp.domain.com",
    port: 465,
    secure: true, // upgrade later with STARTTLS
    auth: {
      user: "registry-help@modelmatcher.net",
      pass: "Dsapiens00!"
    },

  });

transporter.verify(function(error, success) {
    if (error) {
      console.log(error);
    } else {
      console.log("Server is ready to take our messages");
    }})

      // send mail with defined transport object
  let info = transporter.sendMail({
    from: '"Test" <registry-help@modelmatcher.net>', // sender address
    to: "lucianli123@gmail.com", // list of receivers
    subject: "Hello ✔", // Subject line
    text: "Hello world?", // plain text body
    html: "<b>Hello world?</b>", // html body
  });