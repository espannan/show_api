import React from 'react';
import moment from 'moment';

class Show extends React.Component {
  render() {
    var showtime = moment(this.props.data.showtime);
    return <p>
      <b>{showtime.format("MMMM Do YYYY")}:</b> {this.props.data.headliner}
    </p>;
  }
};

class ShowCollection extends React.Component {
  render() {
    const shows = this.props.data.map((showData) => {
      return <Show data={showData} key={showData.id}/>;
    });
    return <div>
      {shows}
    </div>;
  }
};

class Venue extends React.Component {

  render() {

    return (
      <div>
        <h2><a href={this.props.data.url}>{this.props.data.name}</a></h2>
        <ShowCollection data={this.props.data.show_set}/>
      </div>
    );
  }
};

export class VenueCollection extends React.Component {

  render() {
    const venues = this.props.data.map((venueData) => {
      return <Venue data={venueData} key={venueData.name}/>;
    });

    return (
      <div>
        {venues}
      </div>
    );
  }
};