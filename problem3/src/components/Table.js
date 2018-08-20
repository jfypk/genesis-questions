import React, { Component } from 'react';
import _ from "lodash";
import ReactTable from "react-table";
import { Popup } from 'semantic-ui-react';
import 'semantic-ui-css/semantic.min.css';
import 'react-table/react-table.css';

export default class Table extends Component {
    constructor() {
        super();
        this.columns = [];
        this.state = {
            data: [],
            pages: null,
            headers: null,
            loading: true,
            selected: null
        };
        this.fetchData = this.fetchData.bind(this);
        this.requestData = this.requestData.bind(this);
        this.getSummStats = this.getSummStats.bind(this);
    }

    componentDidMount() {
        this.setState({
            data: this.props.data,
            headers: this.props.headers
        });
    }

    //uses lodash to calculate summary stats
    getSummStats(data, key) {
        let z = data[0]
        let count = data.length
        if(z && typeof(z[key]) === "number") {
            let numberColData = _.map(data, d => d[key])
            return (
                <div>
                    <strong>Average: </strong>
                    {_.round(_.mean(numberColData),2)}
                    <br />
                    <strong>Sum: </strong>
                    {_.sum(numberColData)}
                    <br />
                    <strong>Count: </strong>
                    {count}
                    <br />
                    <strong>Max: </strong>
                    {_.max(numberColData)}
                    <br />
                    <strong>Min: </strong>
                    {_.min(numberColData)}
                </div>
                
            )
        } else if (z && typeof(z[key]) === "string") {
            let stringColData = _.map(_.groupBy(data, d=> d[key]), (d, key) => key);
            return (
                <div>
                    <strong>Popular: </strong>
                    {_.first(
                          _.reduce(
                            _.map(_.groupBy(data, d => d[key])),
                            (a, b) => (a.length > b.length ? a : b)
                          )
                        )[key]}
                    <br />
                    <strong>Longest: </strong>
                    {_.reduce(stringColData,
                        (a, b) => (a.length > b.length ? a : b)
                      )}
                      <br />
                    <strong>Shortest: </strong>
                    {_.reduce(stringColData,
                        (a, b) => (a.length < b.length ? a : b)
                      )}
                </div>
            )
        } else {
            return (
                <span>
                    error
                </span>
            )
        }
    }

    //dynamically creates columns based on csv data. Also dynamically creates popup for each cell to show summary statistics and cell information
    getColumns(data) {
        return this.props.headers.map(key => {
            return {
                Header: key,
                id: key,
                accessor: d => d[key],
                Cell: (props) => { return ( 
                    <Popup 
                        header={props.original[key]}
                        trigger={<div>{props.original[key]}</div>} 
                        content={
                            <div>
                                <p>
                                    {"Row: " + props.original["row"] + " | Type: " + typeof(props.original[key])}
                                </p>
                                {this.getSummStats(data, key)}
                                
                            </div>}  
                        size='mini'
                        inverted
                        position='top center'
                /> ); }
            };
        });
    }

    // Whenever the table model changes, or the user sorts or changes pages, this method gets called and passed the current table model.
    fetchData(state, instance) {
        this.setState({ loading: true });
        this.requestData(
            state.pageSize,
            state.page,
            state.sorted,
            state.filtered
        ).then(res => {
            this.setState({
                data: res.rows,
                pages: res.pages,
                loading: false
            });
        });
    }

    //helper method to filter and sort data correctly and return rows and number of pages
    requestData(pageSize, page, sorted, filtered) {
        return new Promise((resolve, reject) => {
            let filteredData = this.props.data;

            if (filtered.length) {
            filteredData = filtered.reduce((filteredSoFar, nextFilter) => {
                return filteredSoFar.filter(row => {
                return (row[nextFilter.id] + "").includes(nextFilter.value);
                });
            }, filteredData);
            }
            
            const sortedData = _.orderBy(
            filteredData,
            sorted.map(sort => {
                return row => {
                if (row[sort.id] === null || row[sort.id] === undefined) {
                    return -Infinity;
                }
                return typeof row[sort.id] === "string"
                    ? row[sort.id].toLowerCase()
                    : row[sort.id];
                };
            }),
            sorted.map(d => (d.desc ? "desc" : "asc"))
            );
            const res = {
                rows: sortedData.slice(pageSize * page, pageSize * page + pageSize),
                pages: Math.ceil(filteredData.length / pageSize)
            };

            setTimeout(() => resolve(res), 500);
        });
    };
    
    render() {
        const { data, pages, loading } = this.state;
        
        //add index column to dataset
        this.columns = this.getColumns(data);
        this.columns.unshift({
            Header: "Index",
            accessor: "row",
            filterable: false,
            maxWidth: 80
        });
        
        return (
            <div className="Table">
            <ReactTable
                    columns={this.columns}
                    data={data}
                    manual
                    noDataText="Upload a CSV file"
                    pages={pages}
                    loading={loading}
                    onFetchData={this.fetchData}
                    filterable
                    style={{
                        height: "100%",
                        width: "100vw"
                    }}
                    defaultPageSize={-1}
                    showPagination={false}
                    className="-striped -highlight"
                    />    
            </div>
        );
    }
}