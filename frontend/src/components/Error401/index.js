import React from 'react';
import {Link} from 'react-router-dom';

const Error404 = () => (
    <div className="app-wrapper page-error-container animated slideInUpTiny animation-duration-3">
        <div className="page-error-content">
            <div className="error-code mb-4 animated zoomInDown">401</div>
            <h2 className="text-center fw-regular title bounceIn animation-delay-10 animated">
                No tienes permisos para ver esta página
            </h2>
            <form className="mb-4" role="search">
                <div className="search-bar shadow flipInX animation-delay-16 animated">
                    <div className="form-group">
                        <input type="search" className="form-control form-control-lg border-0" placeholder="Search..."/>
                        <button className="search-icon">
                            <i className="zmdi zmdi-search zmdi-hc-lg"/>
                        </button>
                    </div>
                </div>
            </form>
            <p className="text-center zoomIn animation-delay-20 animated">
                <Link className="btn btn-primary" to="/app/listado-proceso">Volver</Link>
            </p>
        </div>
    </div>
);

export default Error404;
