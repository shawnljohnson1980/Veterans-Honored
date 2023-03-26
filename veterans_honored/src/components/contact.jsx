import React from "react";
import "../index.css";

const Contact = () => {
  return (
    <div className="container">
      <h5 className="text-white mt-3">Contact Us</h5>
      <div className="col-5 mt-2">
        <form
          action="contactUs"
          method="post"
          className="mb-5 border border-primary border-rounded shadow p-3 opacity-85"
          id="contact-form"
        >
          <div className="form-group ">
            <label for="name" className="p-2">
              Name:
            </label>
            <input
              type="text"
              className="form-control opacity-.75 text-white bg-dark border border-rounded border-primary shadow"
              placeholder="Name"
            ></input>
          </div>
          <div className="form-group ">
            <label for="email" className="p-1">
              Email Address:
            </label>
            <input
              type="email"
              className="form-control opacity-.75 text-white bg-dark border border-rounded border-primary shadow"
              placeholder="Name"
            ></input>
          </div>
          <div className="form-group p-2">
            <label for="phone" className="p-2">
              Phone Number:
            </label>
            <input
              type="tel"
              placeholder="(000)000-0000"
              className=" form-control opacity-.75 text-white bg-dark border border-rounded border-primary shadow"
            ></input>
          </div>
          <div className="form-group p-2">
            <label for="comment" className="text-white p-2 mt-2">
              Comments:
            </label>
            <textarea
              cols="25"
              rows="7"
              placeholder="Your thoughts here..."
              className="form-control opacity-.75 text-white bg-dark border border-rounded border-primary shadow"
            ></textarea>
          </div>
          <div className="form-group p-2">
            <button
              type="submit"
              className="btn btn-primary border border-rounded"
            >
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
export default Contact;
