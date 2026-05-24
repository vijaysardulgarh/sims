import {
    useParams
} from "react-router-dom";

import UserForm from "../components/UserForm";


const EditUserPage = () => {

    const {
        id
    } = useParams();


    return (

        <div>

            <UserForm
                userId={id}
            />

        </div>
    );
};


export default EditUserPage;