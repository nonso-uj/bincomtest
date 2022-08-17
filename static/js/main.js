$(function(){

    $('#add').click(function(){
        $('#addToMe').append(`
        <fieldset class="mb-3">
                            <div class="form-group mb-3">
                            <label class="form-label" for="party_abbreviation[]">party_abbreviation</label>
                            <input class="form-control" type="text" name="party_abbreviation[]" placeholder="party_abbreviation">

                            <label class="form-label" for="party_score[]">party_score</label>
                            <input class="form-control" type="number" name="party_score[]" placeholder="party_score">
                        </div>
                        </fieldset>
        `)
    })
})