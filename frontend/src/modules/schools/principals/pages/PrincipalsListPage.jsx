import { useEffect, useState } from "react";

import principalService from "../services/principalService";

const PrincipalsListPage = () => {

    const [principals, setPrincipals] =
        useState([]);

    useEffect(() => {

        fetchPrincipals();

    }, []);

    const fetchPrincipals = async () => {

        const response =
            await principalService.getPrincipals();

        setPrincipals(
            response.data.results ||
            response.data
        );
    };

    return (

        <div>

            <h2>
                Principals
            </h2>

            <table>

                <thead>

                    <tr>

                        <th>ID</th>

                        <th>School</th>

                        <th>Name</th>

                    </tr>

                </thead>

                <tbody>

                    {principals.map(
                        (principal) => (

                            <tr
                                key={principal.id}
                            >

                                <td>
                                    {principal.id}
                                </td>

                                <td>
                                    {
                                        principal.school_name
                                    }
                                </td>

                                <td>
                                    {
                                        principal.name
                                    }
                                </td>

                            </tr>
                        )
                    )}

                </tbody>

            </table>

        </div>
    );
};

export default PrincipalsListPage;