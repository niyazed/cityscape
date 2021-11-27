const express = require('express')
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const port = process.env.PORT || 3000;

app.listen(port, () => console.log(`[INFO] Listening at ${port}`));
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(express.static('public'));



app.post('/booked', (req, res) => {
    const text = req.body['daterange'].split(" - ")
    const start_date = text[0]
    const end_date = text[1]
    const data = {"email": req.body['email'], "start_date": start_date, "end_date": end_date}
    


    axios.post('http://127.0.0.1:8000/api/v1/reservation/', data)
      .then(function (response) {
        console.log(response);
        res_text = response['data']
        res.json(res_text)
        
      })
      .catch(function (error) {
        console.log(error);
      });

      
    
})