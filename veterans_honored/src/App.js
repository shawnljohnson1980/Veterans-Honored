import React from "react";
import "./App.css";
import { Router } from "@reach/router";
import Home from "./components/home.jsx";
import About from "./components/about.jsx";
import Contact from "./components/contact.jsx";
import "bootstrap/dist/css/bootstrap.min.css";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import "bootstrap/dist/js/bootstrap.bundle.min";
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";
import Member from "./components/member.jsx";
import Donate from "./components/donate.jsx";

function App() {
  return (
    <div className="App">
      <div className="wrapper" style={{ fontFamily: "Regular,Tirto Writter" }}>
        <Navbar className="shadow text-white" bg="dark" expand="lg">
          <Container className="text-white">
            <Navbar.Brand className="text-white" href="/">
              Veterans Honored
            </Navbar.Brand>
            <Navbar.Toggle
              className="text-white"
              aria-controls="basic-navbar-nav"
            />
            <Navbar.Collapse
              className="text-white"
              id="basic-navbar-nav text-white"
            >
              <Nav className="bg-dark text-white">
                <Nav.Link className="text-white" href="/about">
                  About
                </Nav.Link>
                <Nav.Link className="text-white" href="/contact">
                  Contact Us
                </Nav.Link>
                <NavDropdown
                  className="text-white "
                  title="Extras Links"
                  id="basic-nav-dropdown text-white"
                >
                  <NavDropdown.Item
                    className="text-white bg-dark"
                    href="/member"
                  >
                    Membership
                  </NavDropdown.Item>
                  <NavDropdown.Item
                    className="text-white bg-dark"
                    href="/donate"
                  >
                    Donate
                  </NavDropdown.Item>
                </NavDropdown>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>
        {/* This is the Router i.e. This creates the links to the individual components,
     which provide the pages we will see in our app*/}
        <Router>
          {/* This route is for home component */}
          <Home path="/" component={Home} />
          {/* This Route is for about component */}
          <About path="/about" component={About} />
          {/* This Route is for contact component */}
          <Contact path="/contact" component={Contact} />
          {/* This is the Route for member component */}
          <Member path="/member" component={Member} />
          {/* This is the route for the donate component */}
          <Donate path="/donate" component={Donate} />
        </Router>
      </div>
    </div>
  );
}
export default App;
