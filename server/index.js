const express = require("express");
const cors = require("cors");

const PORT = process.env.PORT || 5000;

const app = express();

app.use(express.static("public"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors());

app.post("/test", (req, res) => {
  console.log(req.body);
  res.json({
    result: Math.random() > 0.5 ? "SPAM" : "HAM",
  });
});

app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});
