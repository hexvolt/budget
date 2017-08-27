import React from 'react'
import { connect } from 'react-redux'
import { Redirect } from "react-router-dom";


class EnsureLoggedInContainer extends React.Component {

  componentDidMount() {
    const { dispatch, currentUrl } = this.props;

    if (!this.props.isLoggedIn) {
      // dispatch(setRedirectUrl(currentUrl))
    }
  }

  render() {
    if (this.props.isLoggedIn)
      return this.props.children;

    else
      return <Redirect to={{
        pathname: "/login",
        state: { from: this.props.location}
      }} />
  }
}

const mapStateToProps = (state, ownProps) => ({
  isLoggedIn: state.isLoggedIn,
  currentUrl: ownProps.location.pathname
});

export default connect(mapStateToProps)(EnsureLoggedInContainer);
