import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

var today = new Date();

const minOffset = 0;
const maxOffset = 10;
const thisYear = today.getFullYear();

class DropDownYear extends React.Component {
  handleChange = () => {
    var year = this.dropdown.value
    this.props.onSelectYear(year)
  }
  
  render() {
    const options = [];

    for (let i = minOffset; i <= maxOffset; i++) {
      const year = thisYear + i;
      options.push(<option value={year}>{year}</option>);
    }

    return (
      <select name="year" value={this.selectedYear} onChange={this.handleChange} ref={(ref) => this.dropdown = ref}>
        {options}
      </select>
    );
  }
}

class NameForm extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      diff_range: "e",
      grind_per: "0",
      month: today.getMonth(),
      day: today.getDate(),
      year: today.getFullYear(),
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleYear = (yearValue) => {
    this.setState({year: yearValue});
  }

  handleChange(event) {
    const target = event.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleSubmit(event) {
    alert("My difficulty is " + this.state.diff_range + ". There are " + this.state.grind_per + " days in the grind period chosen. The date start is " + this.state.month + "/" + this.state.day + "/" + this.state.year);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Choose your difficulty range.
          <select name="diff_range" value={this.state.diff_range} onChange={this.handleChange}>
            <option value="e">Easy</option>
            <option value="em">Easy / Medium</option>
            <option value="m">Medium</option>
            <option value="mh">Medium / Hard</option>
            <option value="h">Hard</option>
          </select>
        </label>
        <br />
        <label>
          How many days in grind period?
          <input name="grind_per" type="type" value={this.state.grind_per} onChange={this.handleChange} />
        </label>
        <br />
        <label>
          Choose your start date.
          <select name="month" value={this.state.month} onChange={this.handleChange}>
            <option value="1">January</option>
            <option value="2">February</option>
            <option value="3">March</option>
            <option value="4">April</option>
            <option value="5">May</option>
            <option value="6">June</option>
            <option value="7">July</option>
            <option value="8">August</option>
            <option value="9">September</option>
            <option value="10">October</option>
            <option value="11">November</option>
            <option value="12">December</option>
          </select>
          <select name="day" value={this.state.day} onChange={this.handleChange}>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
            <option value="10">10</option>
            <option value="11">11</option>
            <option value="12">12</option>
            <option value="13">13</option>
            <option value="14">14</option>
            <option value="15">15</option>
            <option value="16">16</option>
            <option value="17">17</option>
            <option value="18">18</option>
            <option value="19">19</option>
            <option value="20">20</option>
            <option value="21">21</option>
            <option value="22">22</option>
            <option value="23">23</option>
            <option value="24">24</option>
            <option value="25">25</option>
            <option value="26">26</option>
            <option value="27">27</option>
            <option value="28">28</option>
            <option value="29">29</option>
            <option value="30">30</option>
            <option value="31">31</option>
          </select>
          ,
          <DropDownYear value={this.state.year} onSelectYear={this.handleYear} />
        </label>
        <br />
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

ReactDOM.render(
  <NameForm />,
  document.getElementById('root')
);
