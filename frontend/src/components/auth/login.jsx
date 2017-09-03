import React from 'react';
import { connect } from 'react-redux'


class LoginForm extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      username: '',
      password: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    const name = event.target.name;
    const value = event.target.value;
    this.setState({
      [name]: value   // merges this param into existing state
    })
  }

  handleSubmit(e) {
    e.preventDefault();
    // need to submit the data to server
    // dispatch an action -> a certain reducer will be triggered, which will
    // update a global store state.
    // But here we don't have a store.dispatch method to invoke.. -
    // that is why a onSubmit method of outer container should be called here,
    // because outer container has an access to sotre.dispatch method.
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          User Name:
          <input name="username" type="text" value={this.state.username} onChange={this.handleChange} /><br/>
        </label>
        <label>
          Password:
          <input name="password" type="text" value={this.state.password} onChange={this.handleChange} /><br/>
        </label>
        <button type="submit">Login</button>
      </form>
    );
  }
}

const mapStateToProps = (state) => {
  return {

  }
};

const mapDispatchToProps = (dispatch) => {
  return {
    onClick: (something) => {
      dispatch()
    }
  }
};

const LoginContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(LoginForm);

export default LoginForm;
