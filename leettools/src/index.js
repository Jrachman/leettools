import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

var today = new Date();

class DropDownMonth extends React.Component {
  constructor(props) {
    super(props);

    this.minOffset = 1;
    this.maxOffset = 12;

    this.state = {
      month: today.getMonth()
    };
  }

  handleChange = () => {
    var month = this.dropdown.value
    this.setState({month: month});
    this.props.onSelectMonth(month)
  }

  render() {
    const options = [];
    //might need to fix this
    for (let i = this.minOffset; i <= this.maxOffset; i++) {
      options.push(<option value={i}>{i}</option>);
    }

    return (
      <select name="month" value={this.state.month} onChange={this.handleChange} ref={(ref) => this.dropdown = ref}>
        {options}
      </select>
    );
  }
}

class DropDownDay extends React.Component {
  constructor(props) {
    super(props);

    this.minOffset = 1;
    this.maxOffset = 31;

    this.state = {
      day: today.getDate()
    };
  }

  handleChange = () => {
    var day = this.dropdown.value
    this.setState({day: day});
    this.props.onSelectDay(day)
  }

  render() {
    const options = [];
    //might need to fix this
    for (let i = this.minOffset; i <= this.maxOffset; i++) {
      options.push(<option value={i}>{i}</option>);
    }

    return (
      <select name="day" value={this.state.day} onChange={this.handleChange} ref={(ref) => this.dropdown = ref}>
        {options}
      </select>
    );
  }
}

class DropDownYear extends React.Component {
  constructor(props) {
    super(props);

    this.minOffset = 0;
    this.maxOffset = 10;
    this.thisYear = today.getFullYear();

    this.state = {
      year: today.getFullYear()
    };
  }

  handleChange = () => {
    var year = this.dropdown.value
    this.setState({year: year});
    this.props.onSelectYear(year)
  }

  render() {
    const options = [];

    for (let i = this.minOffset; i <= this.maxOffset; i++) {
      const year = this.thisYear + i;
      options.push(<option value={year}>{year}</option>);
    }

    return (
      <select name="year" value={this.state.year} onChange={this.handleChange} ref={(ref) => this.dropdown = ref}>
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
      year: today.getFullYear()
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleMonth = (monthValue) => {
    this.setState({month: monthValue});
  }

  handleDay = (dayValue) => {
    this.setState({day: dayValue});
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
    event.preventDefault();
      const data = {
        diff_range: this.state.diff_range,
        grind_per: this.state.grind_per,
        month: this.state.month,
        day: this.state.day,
        year: this.state.year
       };
      console.log('submit');
      console.log(data);
      fetch('http://127.0.0.1:3000/result', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify(data),
      })
        .then(res => res.json())
        .then(res => console.log(res));
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
          <DropDownMonth value={this.state.month} onSelectMonth={this.handleMonth} />
          <DropDownDay value={this.state.day} onSelectDay={this.handleDay} />
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
