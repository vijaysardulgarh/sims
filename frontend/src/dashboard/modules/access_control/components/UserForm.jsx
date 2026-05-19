const UserForm = ({
    isEdit = false
}) => {

    return (

        <div>

            {
                isEdit
                    ? "Edit User Form"
                    : "Add User Form"
            }

        </div>
    );
};

export default UserForm;