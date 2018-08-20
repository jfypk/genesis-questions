import React, { Component } from 'react';
import Table from './Table.js';
import Csvreader from './Csvreader.js';
import '../styles/App.css';

class App extends Component {
  constructor() {
    super();
    this.state = {
      data : null,
      dataReceived: false,
      headers: null
    }
  }

  //call back function to receive data from CSVReader
  dataFromCsvreader = (e) => {
    this.setState({
      data : e.data,
      dataReceived : e.dataLoaded,
      headers: e.headers
    });
  } 

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Genesis Datatable</h1>
        </header>
        <div id="Content">
          {!this.state.dataReceived && <Csvreader dataCallback={this.dataFromCsvreader}/>}
          {this.state.dataReceived && <Table data={this.state.data} headers={this.state.headers}/>}
        </div>
        
      </div>
    );
  }
}

export default App;
