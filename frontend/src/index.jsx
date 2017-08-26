import React from 'react';
import ReactDOM from 'react-dom';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import {
  BrowserRouter,
  Link,
  Route,
  Switch
} from 'react-router-dom';

// const Square = (props) => (
//   <button className="square" onClick={props.onClick}>
//     {props.value}
//   </button>
// );
//
// class Board extends React.Component {
//
//   constructor() {
//     super();
//     this.state = {
//       squares: Array(9).fill(null),
//       xIsNext: true
//     };
//   }
//
//   handleClick(i) {
//     const squares = this.state.squares.slice();
//     if (calculateWinner(squares) || squares[i]) {
//       return;
//     }
//
//     squares[i] = this.state.xIsNext ? 'X' : 'O';
//
//     this.setState({squares: squares, xIsNext: !this.state.xIsNext});
//   }
//
//   renderSquare(i) {
//     return (
//       <Square
//         value={this.state.squares[i]}
//         onClick={() => this.handleClick(i)}
//       />
//     );
//   }
//
//   render() {
//     const winner = calculateWinner(this.state.squares);
//     let status;
//
//     if (winner) {
//       status = 'Winner: ' + winner;
//     } else {
//       status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
//     }
//
//     return (
//       <div>
//         <div className="status">{status}</div>
//         <div className="board-row">
//           {this.renderSquare(0)}
//           {this.renderSquare(1)}
//           {this.renderSquare(2)}
//         </div>
//         <div className="board-row">
//           {this.renderSquare(3)}
//           {this.renderSquare(4)}
//           {this.renderSquare(5)}
//         </div>
//         <div className="board-row">
//           {this.renderSquare(6)}
//           {this.renderSquare(7)}
//           {this.renderSquare(8)}
//         </div>
//       </div>
//     );
//   }
// }
//
// class Game extends React.Component {
//   render() {
//     return (
//       <div className="game">
//         <div className="game-board">
//           <Board />
//         </div>
//         <div className="game-info">
//           <div>{/* status */}</div>
//           <ol>{/* TODO */}</ol>
//         </div>
//       </div>
//     );
//   }
// }
//
// function calculateWinner(squares) {
//   const lines = [
//     [0, 1, 2],
//     [3, 4, 5],
//     [6, 7, 8],
//     [0, 3, 6],
//     [1, 4, 7],
//     [2, 5, 8],
//     [0, 4, 8],
//     [2, 4, 6],
//   ];
//   for (let i = 0; i < lines.length; i++) {
//     const [a, b, c] = lines[i];
//     if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
//       return squares[a];
//     }
//   }
//   return null;
// }

// ========================================
const Home = () => (
  <div>
    <h1>Welcome to budget.</h1>
  </div>
);

const Header = () => (
  <header>
    <nav>
      <li><Link to="/">Home</Link></li>
      <li><Link to="/login">Login</Link></li>
      <li><Link to="/contacts">Contacts</Link></li>
    </nav>
  </header>
);

const Login = () => (
  <form>
    <label>
      Test input
      <input name="test" type="text" value="test" />
    </label>
  </form>
);

const Contacts = () => (
  <div>
    <h1>Contacts.</h1>
    <ul>
      <li>email</li>
      <li>phone</li>
    </ul>
  </div>
);

const Main = () => (
  <main>
    Main section
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/login" component={Login} />
      <Route exact path="/contacts" component={Contacts} />
    </Switch>
  </main>
);


class App extends React.Component {
  render() {
    return (
      <div>
        <Header />
        <Main />
      </div>
    );
  }
}

const rootReducer = (state={}, action) => {
  return {
    ...state
  }
};

ReactDOM.render((
  <Provider store={createStore(rootReducer)}>
    /* makes store available in the context for all children */
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider>
), document.getElementById('root'));