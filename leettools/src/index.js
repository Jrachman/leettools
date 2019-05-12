import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {diff_range: "grapefruit", grind_per: ""};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
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
    alert("My difficulty is " + this.state.diff_range + ". There are " + this.state.grind_per + " days in the grind period chosen.");
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
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

ReactDOM.render(
  <NameForm />,
  document.getElementById('root')
);
