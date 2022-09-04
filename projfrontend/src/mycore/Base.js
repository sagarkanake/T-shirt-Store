import React from "react";

import Menu from "./Menu";
const Base = ({
    title = "My Title",
    description = "My description",
    className = "bg-dark text-white p-4",
    children 
}) => {
    
    return(
      <div>
        <Menu/>
        <div className="container-fluid">
            <div className="jumbotron bg-dark text-white text-center mt-1">
              <h2 className="display-4 pt-4"> {title} </h2>
              <p className="lead pb-4"> {description} </p>
            </div>
            <div className={className}> {children} </div>
        </div>
        <footer className="footer bg-dark mt-auto py-3">
          <div className="container-fluid bg-success text-white text-center py-3">
             <h4> If you got any questions, reach me out at instagram</h4>
             <button className="btn btn-warning btn-lg">Contact-Us</button>
             <div className="container">
                 <span className="text-dark">
                     An Amazing Django React Fullstack Course
                 </span>
             </div>
          </div>
         </footer>
      </div>
    );

}


export default Base;