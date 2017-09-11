import React from 'react';
import { connect } from 'react-redux'
import { checkApiResponseStatus } from "../../common/utils";
import { ErrorList} from "../common/utils";


class LoginForm extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      username: '',
      password: '',
      errors: {}
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    // merge target value into existing state
    this.setState({
      [event.target.name]: event.target.value
    })
  }

  handleSubmit(e) {
    e.preventDefault();

    this.setState({
      ['errors']: {}
    });
    // TODO: validate the data

    // send request to the server
    fetch('/api/auth/login/', {
      method: "POST",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: this.state.username,
        password: this.state.password,
      })
    })
    .then(response => checkApiResponseStatus(response))
    .then(response => response.json())
    .then(data => data.key && this.props.onLoggedIn(data.key))
    .catch(errors => this.setState({['errors']: errors.data}));
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          User Name:
          <input name="username" type="text" value={this.state.username}
                 onChange={this.handleChange} /><br/>
        </label>
        <label>
          Password:
          <input name="password" type="text" value={this.state.password}
                 onChange={this.handleChange} /><br/>
        </label>
        <button type="submit">Login</button>
        <ErrorList errors={this.state.errors.non_field_errors} />
      </form>
    );
  }
}

const mapStateToProps = (state) => {
  console.log(state);
  return {

  }
};

const mapDispatchToProps = (dispatch) => {
  return {
    onLoggedIn: (key) => {
      console.log("Successfully logged in!");
      dispatch({'type': 'LOGGED_IN', 'token': key});
      // TODO: dispatch LOGGED_IN event with the authentication token
    }
  }
};

const LoginContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(LoginForm);

export default LoginContainer;
