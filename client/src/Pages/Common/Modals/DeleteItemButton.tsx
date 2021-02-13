import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import Dialog from '@material-ui/core/Dialog';
import DialogTitle from '@material-ui/core/DialogTitle';
import DeleteForeverIcon from '@material-ui/icons/DeleteForever';
import React, { ReactElement, useState } from 'react';

import LoggedInIconButton from '../LoggedInIconButton';

interface DeleteItemModalProps {
  handleDelete: () => void;
  itemLabel: string; // the name of the individual item being deleted
  itemTypeString: string; // the name of the type of item being deleted
}

// eslint-disable-next-line max-lines-per-function
export default function DeleteItemModal({
  handleDelete,
  itemLabel,
  itemTypeString,
}: DeleteItemModalProps): ReactElement {
  const [confirmationOpen, setConfirmationOpen] = useState(false);

  const handleClose = (confirmed: boolean): void => {
    // close the dialog
    setConfirmationOpen(false);

    // trigger the delete if the user confirmed
    if (confirmed) handleDelete();
  };

  const dialogMessage = `Are you sure you want to delete ${itemLabel}?`;

  return (
    <>
      <LoggedInIconButton
        label={`Delete ${itemTypeString}`}
        onClick={() => setConfirmationOpen(true)}
        ButtonIcon={DeleteForeverIcon}
      />
      <Dialog
        onClose={handleClose}
        aria-labelledby="confirm-action"
        open={confirmationOpen}
      >
        <Box m={2}>
          <DialogTitle id="confirm-dialog-title">{dialogMessage}</DialogTitle>
          <ButtonGroup variant="text" style={{ float: 'right' }}>
            <Button onClick={() => handleClose(false)}>Cancel</Button>
            <Button color="secondary" onClick={() => handleClose(true)}>
              Confirm
            </Button>
          </ButtonGroup>
        </Box>
      </Dialog>
    </>
  );
}
