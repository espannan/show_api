import React from 'react';
import ReactDOM from 'react-dom';
import superagent from "superagent";

import { VenueCollection } from './components.jsx';

let response;
superagent
  .get(`http://127.0.0.1:8000/show-venues/`)
  .set('Content-type', 'application/json')
  .set('Accept', 'application/json')
  .end((err, res) => {
    //response = JSON.parse(res.text);
    debugger
  });
/*
ReactDOM.render(
  <VenueCollection />,
  document.getElementById('root')
);
*/
