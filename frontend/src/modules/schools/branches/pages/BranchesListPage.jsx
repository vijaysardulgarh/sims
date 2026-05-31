import {
    useEffect,
    useState,
} from "react";

import branchService from "../services/branchService";

const BranchesListPage = () => {

    const [branches, setBranches] =
        useState([]);

    useEffect(() => {

        fetchBranches();

    }, []);

    const fetchBranches =
        async () => {

            const response =
                await branchService
                    .getBranches();

            setBranches(
                response.data.results ||
                response.data
            );
        };

    return (

        <div>

            <h2>Branches</h2>

            <table>

                <thead>

                    <tr>

                        <th>ID</th>

                        <th>School</th>

                        <th>Name</th>

                        <th>Code</th>

                        <th>
                            Head Office
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {branches.map(
                        (branch) => (

                            <tr
                                key={branch.id}
                            >

                                <td>
                                    {branch.id}
                                </td>

                                <td>
                                    {
                                        branch.school_name
                                    }
                                </td>

                                <td>
                                    {
                                        branch.name
                                    }
                                </td>

                                <td>
                                    {
                                        branch.code
                                    }
                                </td>

                                <td>
                                    {
                                        branch.is_head_office
                                            ? "Yes"
                                            : "No"
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

export default BranchesListPage;