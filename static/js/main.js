function Break_Line() {
  return <hr style={{ width: "100%", borderStyle: "dashed", marginTop: "60px" }} />;
}

function Card(props) {
  return <div className={props.col}></div>;
}

function Service(props) {
  return <div className="row service">{props.serviceTitle}</div>;
}

function ServiceInfo(props) {
  return (
    <div className="row serviceTitle">
      <b>{props.Res}</b>
    </div>
  );
}

function Section(props) {
  return (
    <section className="row section">
      <Service serviceTitle={props.serviceTitle} />
      <ServiceInfo Res={props.Res} />
      <div className="row">
        <Card col="col col-4" />
        <Card col="col col-4" />
        <Card col="col col-4" />
      </div>
    </section>
  );
}

const container = document.getElementById("root");
const root = ReactDOM.createRoot(container);
root.render(
  <div>
    <Section
      serviceTitle="Our products"
      Res="Best co dsffdsdsf d df"
    />
  </div>
);
  